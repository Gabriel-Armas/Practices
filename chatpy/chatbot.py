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

my_message = "Question: What is the capital of France?"
response = chain.invoke({"question": my_message})
print(response)
