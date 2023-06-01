# chroma
import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./data",
))

collection = client.get_or_create_collection(name="sotu")
print(collection.count())

client.persist()