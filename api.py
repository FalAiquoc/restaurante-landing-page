ro éfrom fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client, Client
import os
from typing import Optional
import httpx

app = FastAPI(title="Nexu Food API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Supabase Config
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://pvwtskdnirubkqpekxti.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "sb_publishable_e_b1oC5BzUZIv-_vPrVdpg_3pm1E5z_")
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class LeadInput(BaseModel):
    nome_estabelecimento: str
    whatsapp: str
    pedidos_por_dia: str

class LeadResponse(BaseModel):
    id: int
    created_at: str
    nome_estabelecimento: str
    whatsapp: str
    pedidos_por_dia: str
    status: str = "novo"

@app.post("/api/leads", response_model=LeadResponse)
async def create_lead(lead: LeadInput):
    """Cria um novo lead e envia notificação para n8n"""
    try:
        # Insere no Supabase
        data = lead.dict()
        result = supabase.table("leads").insert(data).execute()
        
        if not result.data:
            raise HTTPException(status_code=500, detail="Erro ao criar lead")
        
        lead_data = result.data[0]
        
        # Envia webhook para n8n se configurado
        if N8N_WEBHOOK_URL:
            async with httpx.AsyncClient() as client:
                await client.post(
                    N8N_WEBHOOK_URL,
                    json=lead_data,
                    timeout=5.0
                )
        
        return {**lead_data, "status": "created"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/leads")
async def get_leads(limit: int = 50):
    """Lista todos os leads"""
    try:
        result = supabase.table("leads").select("*").limit(limit).execute()
        return {"leads": result.data, "count": len(result.data)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/leads/{lead_id}")
async def get_lead(lead_id: int):
    """Busca um lead específico"""
    try:
        result = supabase.table("leads").select("*").eq("id", lead_id).execute()
        if not result.data:
            raise HTTPException(status_code=404, detail="Lead não encontrado")
        return result.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/webhook/n8n")
async def n8n_webhook(data: dict):
    """Endpoint para receber dados do n8n"""
    try:
        # Processa dados vindos do n8n
        return {"status": "received", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "nexu-food-api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
