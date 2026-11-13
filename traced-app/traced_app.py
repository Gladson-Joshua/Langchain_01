from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI  # noqa: E402

llm = ChatOpenAI(model="gpt-4o-mini")
response = llm.invoke("Give me the details of Gladson Joshua Author of the book missing pieces of business saga")
print(response.content)
