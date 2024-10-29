# Ice Breaker

## 📖 Introdução
O **Ice Breaker** é uma aplicação que utiliza inteligência artificial para gerar resumos e curiosidades sobre perfis profissionais a partir de dados coletados do LinkedIn. A ferramenta integra-se com a API do OpenAI para gerar textos e a biblioteca LangChain para interagir com diversos componentes de linguagem natural. Com ela, você pode facilmente obter informações sobre qualquer pessoa que tenha um perfil no LinkedIn, facilitando interações e networking.

![Captura de tela 2024-10-09 232521](https://github.com/user-attachments/assets/40d5baf1-1444-4d1f-9467-04cb9983f00e)


## 🚀 Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **Flask**: Framework para desenvolvimento web.
- **LangChain**: Framework para aplicações de IA e processamento de linguagem natural.
- **OpenAI**: API utilizada para gerar resumos e insights.
- **dotenv**: Para gerenciamento de variáveis de ambiente.
- **Requests**: Para fazer requisições HTTP.

## 🗂 Estrutura da Pasta

![image](https://github.com/user-attachments/assets/e25cbfc2-214a-4426-a96f-6fabf90f1d2c)


## 🛠 Funcionalidades

### `ice_breaker_with(name: str) -> Tuple[Summary, str]`
Esta função recebe o nome de uma pessoa como parâmetro, procura o perfil no LinkedIn usando o agente `likedin_lookup_agent`, e gera um resumo e duas curiosidades sobre a pessoa.

**Exemplo de uso:**
```python
summary, profile_pic_url = ice_breaker_with(name='Harrison Chase')
```

### `scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False) -> Dict`
Esta função coleta informações de um perfil do LinkedIn. Se mock estiver definido como True, ela retornará dados de um perfil simulado em vez de fazer uma requisição real.

**Exemplo de uso:**
```python
data = scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/eduardoinocencio/')
```
### `lookup(name: str) -> str`
Esta função utiliza o modelo OpenAI para encontrar a URL do perfil LinkedIn de uma pessoa pelo nome. Ela cria um agente que pesquisa no Google.

**Exemplo de uso:**
```python
linkedin_url = lookup(name='Eduardo Inocencio')
```

## 🌐 Integração com Langsmith
A aplicação se integra com LangSmith, permitindo o gerenciamento e a orquestração de fluxos de trabalho complexos com agentes. Essa integração facilita a análise de interações e resultados, melhorando a eficiência e a usabilidade da aplicação.

![Captura de tela 2024-10-09 234401](https://github.com/user-attachments/assets/6c92c027-37ca-46a6-a4c5-495e99683b79)

## 📥 Executando o Projeto
Para executar o projeto, siga as etapas abaixo:

1. Clone o repositório:
```bash
git clone https://seu_repositorio.git
cd ice_breaker
````

2. Instale as dependências
```bash
pip install -r requirements.txt
````

3. Configure o arquivo .env: Crie um arquivo .env na raiz do projeto e adicione suas chaves da API:
```bash
OPENAI_KEY=your_openai_api_key
PROXYCURL_API_KEY=your_proxycurl_api_key
````

4. Execute a aplicação
```bash
python app.py
````

Acesse a aplicação no seu navegador em **http://localhost:5000.**

## 📄 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas.
