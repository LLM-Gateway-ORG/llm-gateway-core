import asyncio

from llm_gateway_core import Chat
from llm_gateway_core.ingest import get_source_processor
from llm_gateway_core.provider.vectorstores import ChromaVectorStore


def main():
    
    ChromaVectorStore(dbpath="goog-20221231.pdf")

async def async_main():
    chat_obj = Chat(
        model_name="groq/gemma2-9b-it",
        sync=False,
        api_key="<api-key>",
    )
    response = await chat_obj.generate([{"role": "user", "content": "How are you?"}])
    async for chunk in response:
        print(chunk.choices[0].delta.content, end="")


asyncio.run(async_main())
