import asyncio
from fastmcp import Client

client = Client("mcpserver.py")

async def call_tool(name :str):
    async with client:
        result = await client.call_tool("hello_hackathon")
        print(result)

asyncio.run(call_tool("Hello"))