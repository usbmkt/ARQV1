# 🚀 Guia de Deploy - Render

## Pré-requisitos

1. **Conta no Render**: [render.com](https://render.com)
2. **Conta no Supabase**: [supabase.com](https://supabase.com)
3. **API Key do Gemini**: [Google AI Studio](https://makersuite.google.com/app/apikey)
4. **Repositório Git**: GitHub, GitLab ou Bitbucket

## 📋 Checklist de Deploy

### ✅ 1. Preparação do Código

- [x] Arquivo `requirements.txt` atualizado
- [x] Arquivo `render.yaml` configurado
- [x] Variáveis de ambiente definidas
- [x] Código testado localmente
- [x] Documentação completa

### ✅ 2. Configuração do Supabase

1. **Criar projeto no Supabase**
2. **Executar script SQL**:
   ```sql
   -- Copie e execute o conteúdo de create_tables.sql
   ```
3. **Configurar RLS (Row Level Security)**
4. **Obter credenciais**:
   - URL do projeto
   - Chave anônima
   - Chave de serviço

### ✅ 3. Configuração do Render

## 🔧 Passo a Passo Detalhado

### 1. Configuração do Supabase

#### Criar Projeto
1. Acesse [supabase.com](https://supabase.com)
2. Clique em "New Project"
3. Escolha organização e nome do projeto
4. Defina senha do banco de dados
5. Selecione região (preferencialmente próxima ao Brasil)

#### Executar Script SQL
1. Vá para "SQL Editor" no painel do Supabase
2. Cole o conteúdo do arquivo `create_tables.sql`
3. Execute o script
4. Verifique se as tabelas foram criadas

#### Obter Credenciais
1. Vá para "Settings" > "API"
2. Copie:
   - **URL**: `https://seu-projeto.supabase.co`
   - **anon key**: Chave pública
   - **service_role key**: Chave privada

### 2. Deploy no Render

#### Conectar Repositório
1. Acesse [render.com](https://render.com)
2. Clique em "New +" > "Web Service"
3. Conecte seu repositório Git
4. Selecione o repositório do projeto

#### Configuração Automática
O Render detectará automaticamente o arquivo `render.yaml` e configurará:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn --bind 0.0.0.0:$PORT src.main:app`
- **Environment**: Python
- **Plan**: Free (ou escolha outro)

#### Configurar Variáveis de Ambiente
No painel do Render, vá para "Environment" e adicione:

```env
GEMINI_API_KEY=AIzaSyBtLYVXxG61tu0CZ4uoLcO8pTWZuGteUFc
SUPABASE_URL=https://albyamqjdopihijsderu.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
DATABASE_URL=postgresql://postgres.albyamqjdopihijsderu:SUA_SENHA@aws-0-us-east-1.pooler.supabase.com:6543/postgres
FLASK_ENV=production
SECRET_KEY=sua-chave-secreta-super-segura
CORS_ORIGINS=*
```

#### Iniciar Deploy
1. Clique em "Create Web Service"
2. Aguarde o build e deploy
3. Acesse a URL fornecida pelo Render

## 🔍 Verificação Pós-Deploy

### 1. Teste Básico
```bash
curl https://seu-app.onrender.com
```

### 2. Teste da API
```bash
curl -X POST https://seu-app.onrender.com/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"nicho": "Teste"}'
```

### 3. Verificar Logs
No painel do Render:
1. Vá para "Logs"
2. Verifique se não há erros
3. Confirme conexão com Supabase

## 🛠️ Configurações Avançadas

### Custom Domain
1. No Render, vá para "Settings"
2. Adicione seu domínio personalizado
3. Configure DNS conforme instruções

### SSL/HTTPS
- Automático no Render
- Certificado Let's Encrypt gratuito

### Monitoramento
1. Configure alertas no Render
2. Monitore uso de recursos
3. Configure backup do Supabase

## 🔧 Troubleshooting

### Problemas Comuns

#### 1. Build Failed
**Erro**: Dependências não instaladas
**Solução**:
```bash
# Verifique requirements.txt
pip freeze > requirements.txt
```

#### 2. Database Connection Error
**Erro**: Não conecta com Supabase
**Solução**:
- Verifique `DATABASE_URL`
- Confirme senha do banco
- Teste conexão local

#### 3. Gemini API Error
**Erro**: API key inválida
**Solução**:
- Verifique `GEMINI_API_KEY`
- Confirme limites de uso
- Teste em ambiente local

#### 4. CORS Error
**Erro**: Blocked by CORS policy
**Solução**:
```python
# Ajuste em src/main.py
CORS(app, origins=['https://seu-dominio.com'])
```

### Logs Úteis

#### Render Logs
```bash
# Visualizar logs em tempo real
render logs --service=seu-servico --tail
```

#### Supabase Logs
1. Vá para "Logs" no painel Supabase
2. Filtre por tipo de log
3. Verifique queries SQL

## 📊 Monitoramento

### Métricas Importantes
- **Response Time**: < 2s
- **Uptime**: > 99%
- **Memory Usage**: < 80%
- **Database Connections**: Monitorar pool

### Alertas Recomendados
1. **High Response Time**: > 5s
2. **High Error Rate**: > 5%
3. **Database Errors**: Qualquer erro
4. **Memory Usage**: > 90%

## 🔄 Atualizações

### Deploy Automático
1. Push para branch principal
2. Render detecta mudanças
3. Build e deploy automático

### Deploy Manual
1. No painel Render
2. Clique em "Manual Deploy"
3. Selecione branch/commit

### Rollback
1. Vá para "Deploys"
2. Selecione deploy anterior
3. Clique em "Redeploy"

## 🔒 Segurança

### Variáveis de Ambiente
- Nunca commite credenciais
- Use variáveis de ambiente
- Rotacione chaves regularmente

### Database Security
- Use RLS no Supabase
- Limite conexões
- Monitor acessos

### API Security
- Rate limiting
- Validação de entrada
- Logs de segurança

## 📈 Otimização

### Performance
```python
# Configurações recomendadas
gunicorn --workers=2 --threads=4 --bind 0.0.0.0:$PORT src.main:app
```

### Caching
```python
# Adicione cache para análises
from flask_caching import Cache
cache = Cache(app)
```

### Database
```sql
-- Índices recomendados
CREATE INDEX idx_analyses_nicho ON analyses(nicho);
CREATE INDEX idx_analyses_created_at ON analyses(created_at DESC);
```

## 📞 Suporte

### Render Support
- [Documentação](https://render.com/docs)
- [Community](https://community.render.com)
- [Status](https://status.render.com)

### Supabase Support
- [Documentação](https://supabase.com/docs)
- [Discord](https://discord.supabase.com)
- [GitHub](https://github.com/supabase/supabase)

---

**✅ Deploy concluído com sucesso!**

Sua aplicação estará disponível em: `https://seu-app.onrender.com`

