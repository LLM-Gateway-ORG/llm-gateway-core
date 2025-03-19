from typing import List

from base import AbstractVectorStore
from langchain_core.documents.base import Document
from langchain_core.embeddings import Embeddings
from langchain_community.vectorstores.chroma import Chroma

from llm_gateway_core.provider.enum import VectorStoreProviderEnum


def get_vector_store(
    type: str, collection: str, embedding: any, **kwargs
) -> AbstractVectorStore:
    if type == VectorStoreProviderEnum.CHROMA:
        return ChromaVectorStore()
    raise Exception("Invalid Vector Store")


class ChromaVectorStore(AbstractVectorStore):
    """
    Reference :- https://github.com/langchain-ai/langchain/issues/15944
    """

    def __init__(self,collection: str, embeddings: Embeddings, *kwargs):
        self.db = Chroma(persist_directory=kwargs.get("persist_directory"))
        super().__init__()
    
    def persist(self, documents: List[Document]):
        return 

    def retrieve(self, ids: List[str]) -> List[Document]:
        # Implement retrieval for Chroma
        pass

