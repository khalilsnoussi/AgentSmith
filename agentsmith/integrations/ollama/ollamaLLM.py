from ollama import Client, AsyncClient
from agentsmith.llms.BaseLLM import BaseLLM
from typing import Optional, Iterator, AsyncIterator
import asyncio
import os

ollama_host = os.getenv("OLLAMA_HOST")


"""
model = "gemma3:4b"
host = "127.0.0.1:8123"
prompt = "can you write some python code that prints hello world"
prompt2 = "can you add something else ?"
prompt3 = "which programming language is this ?"
messages = [{'role': 'user', 'content' : prompt}, {'role':'user', 'content' : prompt2}, {'role' : 'user', 'content':prompt3}]


client = AsyncClient(host= host)
async def generate(prompt : str):
    async for part in await client.generate(model=model, prompt=prompt, stream=True):
        print (part['response'], end = '', flush = True)
        
async def chat(messages : list[str]):
    async for part in await client.chat(model = model , messages = messages, stream= True):
        print(part['message']['content'], end = '', flush = True)

#asyncio.run(generate(prompt=prompt))
asyncio.run(chat(messages=messages))
"""
class Ollama(BaseLLM):
    def __init__(self,
                 host : Optional[str]|None, 
                 model : str,
                 temperature : Optional[float] = 0.7,
                 max_tokens : Optional[int] = None):
        if host:
            self.host = host
        else:
            self.host = os.getenv("OLLAMA_HOST")
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.client = Client(host = self.host)
        self.async_client = AsyncClient(host = self.host)
    
    
    def run(self, prompt : str) -> str:
        return self.client.generate(prompt = prompt, model = self.model)['response']
    

    async def arun(self, prompt : str) -> str: 
        response = await self.async_client.generate(prompt=prompt, model=self.model)
        print(response)
        return response['response']
    
    
            

ollama = Ollama(host = '127.0.0.1:8123', model = "gemma3:4b")
asyncio.run(ollama.arun(prompt="write a hello world python code"))
print("hada tprinta 9bel")
async def main():
    async for chunk in ollama.arun(prompt="write a hello world python code"):
        print(chunk, end='', flush = True)
#asyncio.run(main())

async def main2():
    async for chunk in await ollama.run(prompt= "write a hello world python code"):
        print(chunk, end = '', flush = True)
#asyncio.run(main2())



        
    
            





        
    
    
    
      
    

