#importing all relevant data from libraries
from  langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

#reading the csv file
df = pd.read_csv("restaurant_reviews.csv")

#defining the embedding model
embeddings = OllamaEmbeddings(model="nomic-embed-text")

#setting the database location and checking if the database exists  
db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

# Define search_params before using it
search_params = {
    "k": 15,
    "score_threshold": 0.5
}

#adding the documents to the database if the database does not exist
if add_documents:
    documents = []
    ids = []

    #creating a list of documents and ids   
    #iterating through the rows of the csv file and creating a document for each row
    for i, row in df.iterrows():
        doc = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(doc)

    #creating a vector store if the database does not exist and adding the documents to the database if the database does not exist
    vector_store = Chroma(
        collection_name="restaurant_reviews",
        persist_directory=db_location,
        embedding_function=embeddings
    )
    #adding the documents to the database if the database does not exist
    vector_store.add_documents(documents=documents, ids=ids)
else:
    vector_store = Chroma(
        collection_name="restaurant_reviews",
        persist_directory=db_location,
        embedding_function=embeddings
    )

retriever = vector_store.as_retriever(search_params=search_params)








