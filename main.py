from dotenv import load_dotenv

load_dotenv()

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

tools = [TavilySearch()]
# llm = ChatOpenAI(model="gpt-4",temperature=0)
llm = ChatOllama(model="gpt-oss:20b",temperature=0)
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt=react_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor

def main():
    print("Hello from langchain-course!")
    result = chain.invoke(
        {
            "input": "search in linkedin 3 job postings for an ai engineer in new york and list their results and links",
        }
    )
    print(result)


if __name__ == "__main__":
    main()
