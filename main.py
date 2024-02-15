import asyncio
import aiohttp
import uvicorn
from fastapi import FastAPI

app = FastAPI()

async def get_joke(session, url):
    async with session.get(url) as response:
       return await response.json()


async def get_jokes(urls):
   async with aiohttp.ClientSession() as session:
      tasks = [get_joke(session, url) for url in urls]
      return await asyncio.gather(*tasks)


@app.get('/')
async def root():
    cantidad_faltante = 25
    URL = 'https://api.chucknorris.io/jokes/random'
    unique_items = []
    response_data = []
    while len(unique_items) < cantidad_faltante:
      urls = [URL]*cantidad_faltante
      response = await get_jokes(urls)
      for data in response:
         if data['id'] not in unique_items:
            response_data.append(data)
            unique_items.append(data['id'])
      cantidad_faltante = cantidad_faltante - len(unique_items)
      
    return response

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
