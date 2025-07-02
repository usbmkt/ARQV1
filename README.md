# UP Lançamentos - Arqueologia do Avatar

## 🚀 Visão Geral

O **UP Lançamentos - Arqueologia do Avatar** é um webapp avançado que automatiza a pesquisa de mercado e a geração de estratégias de lançamento para produtos digitais. Utilizando inteligência artificial (Gemini AI), o sistema analisa nichos de mercado, identifica avatares ideais e cria estratégias completas de marketing e vendas.

## ✨ Funcionalidades Principais

### 🎯 Análise Inteligente de Avatar
- **Perfil Psicológico Detalhado**: Criação automática de personas baseadas em dados de mercado
- **Identificação de Dores**: Mapeamento de frustrações e necessidades do público-alvo
- **Análise Comportamental**: Compreensão profunda dos padrões de consumo

### 📊 Dashboard Interativo
- **Visualizações Dinâmicas**: Gráficos e infográficos interativos
- **Métricas em Tempo Real**: Projeções de ROI, conversão e faturamento
- **Relatórios Exportáveis**: Documentos em PDF e formatos editáveis

### 🤖 IA Gemini Integrada
- **Análise Contextual**: Processamento inteligente de dados de mercado
- **Geração de Conteúdo**: Criação automática de materiais de marketing
- **Insights Acionáveis**: Recomendações estratégicas personalizadas

### 🎨 Interface Neomórfica
- **Design Moderno**: Interface 3D com efeitos neomórficos
- **Experiência Imersiva**: Navegação fluida e intuitiva
- **Responsivo**: Compatível com desktop e mobile

## 🛠️ Tecnologias Utilizadas

### Backend
- **Flask**: Framework web Python
- **Gemini AI**: Inteligência artificial do Google
- **Supabase**: Banco de dados PostgreSQL
- **Gunicorn**: Servidor WSGI para produção

### Frontend
- **HTML5/CSS3**: Estrutura e estilização
- **JavaScript ES6+**: Interatividade e funcionalidades
- **Chart.js**: Visualizações e gráficos
- **CSS Neomórfico**: Design 3D moderno

### Infraestrutura
- **Render**: Plataforma de deploy
- **PostgreSQL**: Banco de dados relacional
- **CORS**: Configuração para APIs

## 📁 Estrutura do Projeto

```
arqueologia-avatar-backend/
├── src/
│   ├── static/
│   │   ├── index.html          # Interface principal
│   │   ├── styles.css          # Estilos neomórficos
│   │   ├── script.js           # Lógica frontend
│   │   └── logo.png            # Logo da aplicação
│   ├── routes/
│   │   ├── analysis.py         # Rotas de análise
│   │   └── user.py             # Rotas de usuário
│   ├── models/
│   │   ├── analysis.py         # Modelo de dados
│   │   └── user.py             # Modelo de usuário
│   └── main.py                 # Aplicação principal
├── requirements.txt            # Dependências Python
├── render.yaml                 # Configuração Render
├── create_tables.sql           # Script SQL
├── .env                        # Variáveis de ambiente
└── README.md                   # Documentação
```

## 🚀 Instalação e Configuração

### Pré-requisitos
- Python 3.11+
- Conta no Supabase
- API Key do Gemini AI
- Conta no Render (para deploy)

### Configuração Local

1. **Clone o repositório**
```bash
git clone <repository-url>
cd arqueologia-avatar-backend
```

2. **Crie o ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite o arquivo .env com suas credenciais
```

5. **Execute a aplicação**
```bash
python src/main.py
```

### Configuração do Supabase

1. **Crie as tabelas**
```sql
-- Execute o script create_tables.sql no Supabase
```

2. **Configure as políticas RLS**
```sql
-- As políticas estão incluídas no script SQL
```

## 🌐 Deploy no Render

### Configuração Automática

1. **Conecte o repositório ao Render**
2. **Configure as variáveis de ambiente**:
   - `GEMINI_API_KEY`: Sua chave da API Gemini
   - `SUPABASE_URL`: URL do seu projeto Supabase
   - `SUPABASE_SERVICE_ROLE_KEY`: Chave de serviço do Supabase
   - `DATABASE_URL`: String de conexão PostgreSQL

3. **Deploy automático**
   - O Render utilizará o arquivo `render.yaml` para configuração

### Variáveis de Ambiente Necessárias

```env
GEMINI_API_KEY=sua_chave_gemini
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_ANON_KEY=sua_chave_anon
SUPABASE_SERVICE_ROLE_KEY=sua_chave_service
DATABASE_URL=postgresql://...
FLASK_ENV=production
SECRET_KEY=sua_chave_secreta
CORS_ORIGINS=*
```

## 📊 API Endpoints

### Análise de Mercado
```http
POST /api/analyze
Content-Type: application/json

{
  "nicho": "Neuroeducação",
  "produto": "Pais Líderes, Filhos Vencedores",
  "descricao": "Curso sobre neuroeducação...",
  "preco": "997",
  "publico": "Pais de 30-45 anos",
  "concorrentes": "Lista de concorrentes...",
  "dadosAdicionais": "Informações extras..."
}
```

### Listar Análises
```http
GET /api/analyses?limit=10&nicho=Neuroeducação
```

### Buscar Análise Específica
```http
GET /api/analyses/{id}
```

### Listar Nichos
```http
GET /api/nichos
```

## 🎨 Personalização Visual

### Cores Principais
- **Primária**: `#ff6b35` (Laranja vibrante)
- **Secundária**: `#f7931e` (Laranja dourado)
- **Accent**: `#ff4757` (Vermelho coral)
- **Background**: `#0f172a` (Azul escuro)

### Tipografia
- **Principal**: Inter (Google Fonts)
- **Código**: JetBrains Mono

### Efeitos Neomórficos
- **Sombras**: Múltiplas camadas para profundidade
- **Bordas**: Raios arredondados consistentes
- **Gradientes**: Transições suaves entre cores

## 📈 Funcionalidades do Dashboard

### Métricas Principais
- **Leads Projetados**: Estimativa baseada em dados de mercado
- **Taxa de Conversão**: Cálculo realista para o nicho
- **Faturamento Projetado**: Projeção financeira detalhada
- **ROI Esperado**: Retorno sobre investimento

### Visualizações
- **Gráfico de Pizza**: Distribuição de investimento
- **Gráfico de Barras**: Análise competitiva
- **Funil de Vendas**: Visualização do processo de conversão
- **Timeline**: Cronograma de execução

### Exportação
- **PDF**: Relatório completo para impressão
- **Compartilhamento**: Links diretos para resultados
- **Download**: Dados em formato texto

## 🔧 Desenvolvimento

### Estrutura de Dados

#### Análise
```python
{
  "avatar": {
    "nome": "Nome do Avatar",
    "contexto": "Contexto detalhado",
    "barreira_critica": "Principal obstáculo",
    "estado_desejado": "Objetivo final",
    "frustracoes": ["Lista", "de", "frustrações"],
    "crenca_limitante": "Crença que limita"
  },
  "positioning": {
    "declaracao": "Declaração de posicionamento",
    "angulos": [
      {
        "tipo": "Lógico",
        "mensagem": "Mensagem lógica"
      }
    ]
  },
  "metrics": {
    "leads_projetados": 2500,
    "conversao": 1.5,
    "faturamento": 37500,
    "roi": 89
  }
}
```

### Adicionando Novos Recursos

1. **Backend**: Adicione rotas em `src/routes/`
2. **Frontend**: Implemente em `src/static/script.js`
3. **Estilos**: Adicione CSS em `src/static/styles.css`
4. **Banco**: Atualize modelos em `src/models/`

## 🧪 Testes

### Testes Locais
```bash
# Teste com Flask development server
python src/main.py

# Teste com Gunicorn
gunicorn --bind 0.0.0.0:8000 src.main:app
```

### Testes de API
```bash
# Teste endpoint de análise
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"nicho": "Teste"}'
```

## 🔒 Segurança

### Configurações
- **CORS**: Configurado para produção
- **Environment Variables**: Credenciais protegidas
- **RLS**: Row Level Security no Supabase
- **HTTPS**: Forçado em produção

### Boas Práticas
- Validação de entrada em todas as rotas
- Sanitização de dados do usuário
- Rate limiting (recomendado para produção)
- Logs de segurança

## 📞 Suporte

### Problemas Comuns

1. **Erro de conexão com Supabase**
   - Verifique as credenciais no `.env`
   - Confirme se o banco está ativo

2. **API Gemini não responde**
   - Verifique a chave da API
   - Confirme os limites de uso

3. **Erro de CORS**
   - Verifique a configuração de CORS
   - Confirme os domínios permitidos

### Logs
```bash
# Visualizar logs do Render
render logs --service=seu-servico

# Logs locais
tail -f logs/app.log
```

## 🚀 Roadmap

### Versão 2.0
- [ ] Autenticação de usuários
- [ ] Múltiplos projetos por usuário
- [ ] Integração com redes sociais
- [ ] API para terceiros

### Versão 2.1
- [ ] Análise de sentimento
- [ ] Previsões com ML
- [ ] Relatórios avançados
- [ ] Mobile app

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

---

**Desenvolvido com ❤️ para revolucionar o marketing digital**

