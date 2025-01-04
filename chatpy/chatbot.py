from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the following question:
Question: {question}
Answer:
"""

model = OllamaLLM(model = "llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    print("Type 'exit' to quit the conversation.")
    user_input = input("You: ")
    while user_input.lower() != "exit":
        response = chain.invoke({"question": user_input})
        print("Bot:", response)
        user_input = input("You: ")
    print("Goodbye!")

if __name__ == "__main__":
    handle_conversation()