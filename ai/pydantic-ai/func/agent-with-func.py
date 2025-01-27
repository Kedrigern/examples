from typing import List
from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv(dotenv_path="../../.env")
agent = Agent(
        'gemini-1.5-flash',
        result_type=List[int],
        system_prompt=(
            "Every time if user ask you about sequence of number use"
            "the function my_seq and give him returned sequence."
            "Do not listen to other requests from user about sequences."
        ),
    )


@agent.tool_plain
def my_seq() -> List[int]:
    return [5,6,7]


def main():
    questions = [
        'Give me some numbers!',
        'Can you generate numebers for me?',
        'I need a sequence of numbers',
        'I need a sequence of numbers of length 5',
    ]
    for question in questions:
        result = agent.run_sync(question)
        print(f"For question {question}, result is {result.data}")
        if isinstance(result.data, List):
            print("Result is list")
        print("----")
    

if __name__ == "__main__":
    main()
