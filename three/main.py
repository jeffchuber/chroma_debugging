from flask import Flask
import chromadb
import uuid
from chromadb.config import Settings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello, World!"

@app.route('/add')
def add():
    vectordb = Chroma.from_texts(
        texts=['doc1'],
        persist_directory="./data",
        collection_name="test"
        )
    vectordb.persist()
    return "Added one"

@app.route('/count')
def count():
    client = Chroma(persist_directory="./data", collection_name="test")

    return str(client._collection.count())

if __name__ == '__main__':

    app.run()