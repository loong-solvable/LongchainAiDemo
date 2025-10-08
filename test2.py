from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
_ = load_dotenv()

llm = ChatOpenAI(
    model = "glm-4-flash",
    api_key="9f5e340b0c3345d89a5ad64c1532a9e2.qvXoelXtOSaqN4zP",
    base_url="https://open.bigmodel.cn/api/paas/v4/",

    temperature=0

)

from langchain.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser




prompt = ChatPromptTemplate([
    ("system","你是世界级的高冷御姐"),
    ("human","{input}")
])

output = StrOutputParser()

chain = prompt | llm | output

result = chain.invoke({"input" : "阐述印度和英国之间的关系"})

print(result)
