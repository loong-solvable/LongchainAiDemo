from langchain_core.messages import HumanMessage,SystemMessage
from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    model = "deepseek-chat",
    temperature=0,
    max_tokens=1024,
    api_key="sk-a8cee46b1c63404ba82cd671f4de4660"
)

messages = [

    SystemMessage(content="你是一个乐于助人的可爱女友，回答要温柔精准"),
    HumanMessage(content="何为生？何为死？")

]




try:
    response = llm.invoke(messages)
    print("AI回复: ",response.content)

    print("\nstream::")
    for chunk in llm.stream([HumanMessage("何为生？何为死？")]):
        print(chunk.content,end="",flush=True)
except Exception as e:
    print(f"调用出错: {e}")