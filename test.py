# A short python code to implement a chatbot - using "Mistral" model . Question already provided to the bot .
import langchain
import ollama

stream = ollama.chat(
    model = 'mistral',
    messages= [{'role':'user','content':'Why is the sky blue?'}],
    stream = True,
)

for chunk in stream:
    print(chunk['message']['content'],end = '', flush =True )
