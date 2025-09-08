from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os


load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key,
    temperature=0.7,
)
parser = StrOutputParser()
chain = llm | parser


def generate_response(messages):
    """Stream response from LLM given chat history."""
    try:
        stream = llm.stream(messages)
        response = ""
        for chunk in stream:
            response += chunk.content
            yield response  
    except Exception as e:
        yield f"⚠️ Error: {e}"
