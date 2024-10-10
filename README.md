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

IceBreaker/
│
├── main.py                  # Arquivo principal para execução da aplicação
├── IceBreaker.py            # Lógica principal do Ice Breaker
├── requirements.txt         # Lista de dependências do projeto
├── tools/                   # Pasta com ferramentas auxiliares
│   ├── __init__.py         
│   └── tools.py             # Funções auxiliares para busca de perfis
├── templates/               # Pasta com os templates HTML
│   └── index.html           # Página inicial da aplicação
├── .env                     # Arquivo para variáveis de ambiente
└── README.md                # Este arquivo