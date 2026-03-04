#!/bin/bash

# Script de instalação da Evolution API para VM DoboyTech
# Execute com: sudo bash install-evolution.sh

set -e

echo "========================================"
echo "  Evolution API - Instalação DoboyTech"
echo "========================================"
echo ""

# 1. Atualizar sistema
echo "[1/6] Atualizando sistema..."
apt-get update -qq
apt-get upgrade -y -qq

# 2. Instalar Docker se não estiver instalado
if ! command -v docker &> /dev/null; then
    echo "[2/6] Instalando Docker..."
    curl -fsSL https://get.docker.com | sh
    systemctl enable docker
    systemctl start docker
else
    echo "[2/6] Docker já instalado ✓"
fi

# 3. Gerar API Key segura
echo "[3/6] Gerando API Key..."
API_KEY=$(openssl rand -hex 32)
echo "API Key gerada: $API_KEY"
echo "⚠️  SALVE ESTA CHAVE! Você precisará dela."
echo ""

# 4. Criar diretório para dados
echo "[4/6] Criando estrutura de diretórios..."
mkdir -p /opt/evolution-api/data
mkdir -p /opt/evolution-api/instances

# 5. Parar container antigo se existir
echo "[5/6] Verificando containers existentes..."
docker stop evolution_api 2>/dev/null || true
docker rm evolution_api 2>/dev/null || true

# 6. Iniciar Evolution API
echo "[6/6] Iniciando Evolution API..."
docker run -d \
  --name evolution_api \
  --restart unless-stopped \
  -p 8080:8080 \
  -e AUTHENTICATION_API_KEY="$API_KEY" \
  -e SERVER_URL="http://34.23.170.134:8080" \
  -e CONFIG_SESSION_PHONE_CLIENT="DoboyTech" \
  -e CONFIG_SESSION_PHONE_VERSION="2.3000.1032750324" \
  -v /opt/evolution-api/data:/evolution/store \
  -v /opt/evolution-api/instances:/evolution/instances \
  atendai/evolution-api:latest

echo ""
echo "========================================"
echo "  ✓ Instalação concluída com sucesso!"
echo "========================================"
echo ""
echo "📋 Informações importantes:"
echo ""
echo "URL da API: http://34.23.170.134:8080"
echo "API Key: $API_KEY"
echo ""
echo "Manager: http://34.23.170.134:8080/manager"
echo "Swagger Docs: http://34.23.170.134:8080/docs"
echo ""
echo "Para ver logs: docker logs -f evolution_api"
echo "Para reiniciar: docker restart evolution_api"
echo ""
echo "⚠️  Salve a API Key em local seguro!"
echo "Ela foi salva em: /opt/evolution-api/api-key.txt"
echo ""

# Salvar API key em arquivo
echo "$API_KEY" > /opt/evolution-api/api-key.txt
chmod 600 /opt/evolution-api/api-key.txt

# Aguardar inicialização
echo "Aguardando API inicializar..."
sleep 5

# Testar se API está respondendo
if curl -s http://localhost:8080 | grep -q "Evolution API"; then
    echo "✓ API está rodando corretamente!"
    docker logs evolution_api --tail 20
else
    echo "⚠️  API pode não ter iniciado corretamente."
    echo "Verifique os logs: docker logs evolution_api"
fi

echo ""
echo "========================================"
echo "Próximos passos:"
echo "1. Anote a API Key acima"
echo "2. Configure o firewall para porta 8080"
echo "3. Acesse: https://falaiquoc.github.io/restaurante-landing-page/whatsapp-qrcode.html"
echo "4. Cole a API Key e gere o QR Code"
echo "========================================"
echo ""
