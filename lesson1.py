from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="deepseek-r1:1.5b", 
    temperature=0.3)  # Set temperature ke 0.7

# response = llm.invoke("Apa itu AI Agent?")
# response = llm.batch(["hallo apa kabar ?", "Jelaskan Tentang perbedaan GenI dan AgenticAI"])
response   = llm.stream("Write a poem about AI")
# print(response)

for chunk in response:
    print(chunk, end="", flush=True)
