# Modelo de Skill Alexa para integrar os modelos da [GroqCloud](https://console.groq.com)
Usei o LLama 3 versão 8B na Alexa 😊  

# Instruções
- Crie uma conta e uma chave de autenticação na Groq cloud: [GrqCLoud](https://console.groq.com)
- Precisa de crédito não fihh, a gente é econômico
  
- Crie uma Skill Alexa-hosted (Python) na Alexa: https://developer.amazon.com/alexa/console/ask/create-new-skill
  - Name your Skill: Escolha um nome de sua preferência (Ex: alexinha)
  - Choose a primary locale: Portuguese (BR)  
  - Em tipo de experiência selecione: Other > Custom > Alexa-hosted (Python)  
  - Hosting region: Pode deixar o padrão (US East (N. Virginia))
  - Templates: Clique em Import Skill
  - Insira o endereço: https://github.com/AlcivanLucas/Alexa_Skill_Groq.git

- Vá na aba "Code"
- Insira sua chave no código: lambda > lambda_function.py:
  ```python
  groq.api_key = "substitua-por-sua-api-key-da-openai"
  ```
- Modifique no mesmo arquivo (lambda_function.py) pro modelo de sua preferência:
  ```python
  MODEL = "llama3b"
  ```
  Exemplos: "llama 3b", "gemma 2", "gemma 7b "  
  [veja a lista completa de modelos aqui](https://console.groq.com/docs/models)

- Salve as alterações

- Faça Build do Modelo e Deploy do Código.

- Seja feliz! 
