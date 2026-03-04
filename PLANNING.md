# Planejamento do Projeto Agêntico - Nexu Food
**Última atualização:** 04/03/2026 | **Status geral:** Em andamento ativo

---

## ✅ Fase 1: Implementação da Camada de Inteligência [CONCLUÍDO PARCIAL]
- ✅ Desenvolvimento do bot.py com classe NexuFoodAgent (agente único multi-função).
- ✅ Lógica de processamento de mensagens (atendimento, cardápio, pedidos).
- ✅ Simulação de multi-agentes: Atendimento, Cardápio e Logística dentro da mesma classe.
- ⏳ Integração real com Gemini API para NLP avançado (próxima iteração).

## ✅ Fase 2: Dashboard Administrativo e Visualização [CONCLUÍDO]
- ✅ Estruturação do dashboard.html com UI moderna (tema Nexu: vermelho/branco).
- ✅ Integração do Chart.js para gráficos de faturamento e volume de pedidos.
- ✅ Status em tempo real dos 3 agentes (Comercial, Cardápio, Logística).
- ✅ Métricas KPI: Leads do dia, Conversão, Tickets IA, Economia estimada.
- ✅ Linkagem estratégica entre Landing Page e Dashboard (/dashboard.html).

## ✅ Fase 3: SEO e Captação de Clientes SaaS [CONCLUÍDO]
- ✅ Landing page profissional com hero section, funcionalidades e pricing.
- ✅ Formulário de trial gratuito com campos: Nome, Email, WhatsApp, Restaurante, Volume de pedidos, Faturamento.
- ✅ Planos definidos: Nexu Start (R$299/mês) e Nexu Advanced (R$399/mês).
- ✅ Seção de tecnologia: Atendimento Virtual IA, Cardápio Dinâmico, Dashboards Reais.
- ✅ Copy focada em benefícios: "+80% de lucro", "40k+ clientes", "24/7 Suporte VIP".

## ⏳ Fase 4: Integração Contínua e Escala [EM ANDAMENTO]
- ⏳ Documentação técnica detalhada (README/STACK) para novos desenvolvedores.
- ⏳ Plano de migração para infraestrutura em nuvem (Railway/Render) para execução permanente dos scripts Python.
- ⏳ Configurar GitHub Actions para CI/CD automático.

## 🚀 Fase 5: Backend e Persistência [PRÓXIMOS PASSOS - PRIORIDADE ALTA]

### 5.1 - Integração Supabase (Semana 1)
- [ ] Criar projeto no Supabase (nexu-food-leads).
- [ ] Tabela `leads`: id, nome, email, whatsapp, restaurante, pedidos_dia, faturamento, plano_interesse, criado_em.
- [ ] Conectar o formulário da landing page ao Supabase via JavaScript (fetch API).
- [ ] Exibir leads no Dashboard Admin em tempo real.

### 5.2 - API Python Intermediária (Semana 2)
- [ ] Criar FastAPI ou Flask com endpoint POST /lead para receber os dados do formulário.
- [ ] Endpoint GET /leads para listar todos os leads do CRM.
- [ ] Integrar bot.py com a API para enriquecer leads automaticamente.
- [ ] Deploy da API no Railway (gratuito até 500h/mês).

### 5.3 - Webhooks e Notificações (Semana 3)
- [ ] Webhook automático: novo lead → mensagem no WhatsApp do dono (via Evolution API ou Z-API).
- [ ] Notificação em tempo real no Dashboard quando um novo lead entra.
- [ ] Integração com N8N para automações avançadas (opcional).

---

## 📊 Estado Atual dos Arquivos
| Arquivo | Status | Descrição |
|---|---|---|
| index.html | ✅ Produção | Landing page completa, formulário de trial, planos |
| dashboard.html | ✅ Produção | Dashboard admin com KPIs e gráficos |
| bot.py | ✅ Local | Agente Python com atendimento, cardápio e logística |
| PLANNING.md | ✅ Atualizado | Este arquivo |
| STACK.md | ✅ Documentado | Stack técnico completo |

## 🔗 Links do Projeto
- **Landing Page:** https://falaiquoc.github.io/restaurante-landing-page/
- **Dashboard:** https://falaiquoc.github.io/restaurante-landing-page/dashboard.html
- **Repositório:** https://github.com/FalAiquoc/restaurante-landing-page
- **Notion:** https://notion.so (Projetos → Nexu Food)
