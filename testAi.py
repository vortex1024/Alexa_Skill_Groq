# 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
#parece que o script do hhtpx foi instalado em um diretorio difreente  /home/galingds/.local/bin
# export GROQ_API_KEY=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

import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "quais os diferencias de usar o modelo de IA da groq",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)