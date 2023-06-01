from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    import chromadb
    from chromadb.config import Settings

    client = chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="./data",
    ))

    collection = client.get_or_create_collection(name="sotu")
    return str(collection.count())

if __name__ == '__main__':
    app.run()