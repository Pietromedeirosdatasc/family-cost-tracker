import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Family Cost Tracker",
    page_icon="💰",
    layout="wide"
)

# Título principal
st.title("🏠 Family Cost Tracker")

st.markdown("""
## Aplicação Python para Rastreamento de Custos Familiares

Esta aplicação oferece:

### 🎯 Dashboard Interativo
- Métricas financeiras em tempo real
- Visualizações avançadas com gráficos
- Indicadores de performance (KPIs)

### 🤖 Machine Learning
- Previsão de custos futuros
- Múltiplos algoritmos de ML
- Análise de tendências

### 📊 Gráficos e Visualizações
- Gráficos de pizza para distribuição por categoria
- Gráficos de barras para gastos mensais
- Gráficos de linha para tendências temporais

### 📝 Interface para Adicionar Gastos
- Formulário intuitivo
- Categorização automática
- Validação de dados

### 🔗 Integração Google Sheets
- Coleta de dados em tempo real
- Sincronização automática
- Backup na nuvem

### 🛠️ Tecnologias Utilizadas:
- **Streamlit** - Interface web
- **Pandas** - Manipulação de dados
- **Plotly** - Visualizações interativas
- **Scikit-learn** - Machine Learning
- **Google Sheets API** - Integração de dados
""")

st.success("Aplicação criada com sucesso! 🎉")
