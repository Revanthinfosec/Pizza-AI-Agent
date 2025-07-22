from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

#defining the model
model = OllamaLLM(model="llama3")

# defining the prompt
template = """
You are an expert in answering the questions about the pizza in a resturateur.

You are given some information about the pizza in a resturateur: {reviews}

Here is the question: {question}

Answer the question based on the information provided.
"""

#defining the prompt template
prompt = ChatPromptTemplate.from_template(template)

#defining the chain with the prompt and the model
chain = prompt | model

#testing the chain with the prompt and the model
chain.invoke({"reviews": "The pizza is good", "question": "What is the best pizza in the restaurant?"})

#looping through the chain with the prompt and the model
while True:
    print("\n\n--------------------------------\n\n")       
    question = input("Enter a question (type 'exit' to quit): ")
    print("\n\n--------------------------------\n\n")       
    if question == "exit":
        break


    #getting the documents from the retriever
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews":reviews, "question": question})
    print(result)







