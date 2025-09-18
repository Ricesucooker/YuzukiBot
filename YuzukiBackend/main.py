from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="Ricesucooker/Yuzuki",)

message =[
    ("hello")
]

resp_msg = llm.invoke(message)
resp_msg
print(resp_msg.content)