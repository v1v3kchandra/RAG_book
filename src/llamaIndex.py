from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

# Use a local embedding model
embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load the local Ollama model
llm = Ollama(model="llama3.2")

# Load documents
documents = SimpleDirectoryReader("../data").load_data()

# Create an index with the local embedding model
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

# Attach the local LLM
query_engine = index.as_query_engine(llm=llm)

# Run a query
response = query_engine.query("What is Italian seasoning?") # PAge 18
print(response)
