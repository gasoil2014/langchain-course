from dotenv import load_dotenv

load_dotenv()

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4o-mini")
structured_llm = llm.with_structured_output(AgentResponse)

#llm = ChatOllama(model="gpt-oss:20b",temperature=0)
#react_prompt = hub.pull("hwchase17/react")

react_prompt_with_format_instructions = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=["input", "agent_scratchpad", "tool_names","tools"],
).partial(format_instructions="")


agent = create_react_agent(llm, tools, prompt=react_prompt_with_format_instructions)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

extract_output = RunnableLambda(lambda x: x["output"])

chain = agent_executor | extract_output | structured_llm

def main():
    print("Hello from langchain-course!")
    result = chain.invoke(
        {
            "input": "decime los principales servicios de la empresa primetec.com.ar",
        }
    )
    print(result)


if __name__ == "__main__":
    main()
