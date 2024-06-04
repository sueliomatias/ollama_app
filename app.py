from langchain_community.llms import Ollama

llm = Ollama(model="phi3", base_url="http://ollama:11434")

response = llm.invoke("O que são Large Language Models?")

print(response)