from dotenv import load_dotenv
from pydantic_ai import Agent

def get_agent() -> Agent:
    #agent = Agent('openai:gpt-4o-mini')
    #agent = Agent('gemini-1.5-flash')
    #agent = Agent('claude-3-5-sonnet-latest')
    agent = Agent('groq:llama-3.3-70b-versatile')
    return agent

def main():
    load_dotenv(dotenv_path="../../.env")

    agent = get_agent()

    try:
        result_sync = agent.run_sync('What is the capital of Italy?')
        print(result_sync.data)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
