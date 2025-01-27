from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_ai import Agent


class CityLocation(BaseModel):
    city: str
    country: str


def main():
    load_dotenv(dotenv_path="../../.env")
    agent = Agent('gemini-1.5-flash', result_type=CityLocation)
    result = agent.run_sync('Where were the olympics held in 2012?')
    print(result.data)
    #> city='London' country='United Kingdom'
    print(result.usage())
    """
    Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65, details=None)
    """


if __name__ == "__main__":
    main()
