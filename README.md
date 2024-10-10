# Ice Breaker

## 📖 Introdução
O **Ice Breaker** é uma aplicação que utiliza inteligência artificial para gerar resumos e curiosidades sobre perfis profissionais a partir de dados coletados do LinkedIn. A ferramenta integra-se com a API do OpenAI para gerar textos e a biblioteca LangChain para interagir com diversos componentes de linguagem natural. Com ela, você pode facilmente obter informações sobre qualquer pessoa que tenha um perfil no LinkedIn, facilitando interações e networking.

## 🚀 Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **Flask**: Framework para desenvolvimento web.
- **LangChain**: Framework para aplicações de IA e processamento de linguagem natural.
- **OpenAI**: API utilizada para gerar resumos e insights.
- **dotenv**: Para gerenciamento de variáveis de ambiente.
- **Requests**: Para fazer requisições HTTP.

## 🗂 Estrutura da Pasta

ice_breaker/ │ ├── app.py # Arquivo principal da aplicação Flask. ├── IceBreaker.py # Contém a lógica principal do Ice Breaker. ├── tools/ # Diretório com funções auxiliares. │ └── tools.py # Contém funções para obter URLs de perfil. ├── templates/ # Diretório para templates HTML. │ └── index.html # Página principal da aplicação. ├── .env # Arquivo para variáveis de ambiente. └── README.md # Este arquivo.