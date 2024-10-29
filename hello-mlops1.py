import os
import openai
import getpass
print("hello mlops1 team -- welcome!")

os.environ["OPENAI_API_KEY"] = getpass.getpass("Please enter your OpenAI API Key: ")
openai.api_key = os.environ["OPENAI_API_KEY"]
print("openai api key <begin>" + openai.api_key + "<end>\n")
from openai import OpenAI
client = OpenAI()

YOUR_PROMPT = "What is the difference between finetuning and RAG?"

client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role" : "user", "content" : YOUR_PROMPT}]
)

from IPython.display import display, Markdown

def get_response(client: OpenAI, messages: str, model: str = "gpt-4o") -> str:
    return client.chat.completions.create(
        model=model,
        messages=messages
    )

def system_prompt(message: str) -> dict:
    return {"role": "system", "content": message}

def assistant_prompt(message: str) -> dict:
    return {"role": "assistant", "content": message}

def user_prompt(message: str) -> dict:
    return {"role": "user", "content": message}

def pretty_print(message: str) -> str:
    display(Markdown(message.choices[0].message.content))
    
messages = [user_prompt(YOUR_PROMPT)]
print(messages)
chatgpt_response = get_response(client, messages)
print("got response")
print(chatgpt_response)
pretty_print(chatgpt_response)