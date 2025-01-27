from typing import List
from dotenv import load_dotenv
from pydantic_ai import Agent

from knowledge import KnowledgeBase

system_promt = """
You are an experienced car sales consultant. Your goal is to match customers with their ideal vehicle while providing excellent service.

You have access to three knowledge base functions:
1. `KnowledgeBase.overview()` - Provides a complete list of available car models and their basic specifications
2. `KnowledgeBase.models(model_name: str)` - Returns detailed information about a specific car model
3. `KnowledgeBase.loan(down_payment: int, target_amount: int)` - Calculates monthly payments for financing options

Process for helping customers:
1. First, use `KnowledgeBase.overview()` to identify potential matches based on customer needs
2. For promising matches, use `KnowledgeBase.models()` to verify the vehicle meets all customer requirements
3. If the customer needs financing, use `KnowledgeBase.loan()` to calculate affordable payment options

Response format:
Model: [Car model name]
Price: [Base price]
Why this is a great match: [2-3 sentences explaining how this vehicle specifically meets the customer's needs]

Always maintain professional courtesy and provide direct, relevant recommendations focused on the customer's requirements.
"""
load_dotenv(dotenv_path="../../.env")

agent = Agent(
        'gemini-1.5-flash',
        system_prompt=system_promt,
        tools=[KnowledgeBase.overview, KnowledgeBase.models, KnowledgeBase.loan]
    )


def main():
    simple_questions = [
        'I need huge lorry',
        'I am single business man and I need fast and sexy car for fun and good representation.',
        'Hello, we are family of 6 which need car for daily commuting and holidays',
        'Hi, we are family of 4 living in the mouintains, so we need 4x4 car. Our budget is 900 000',
        'Hi, we are family of 4 living in the mouintains, so we need 4x4 car. Our budget is 500 000'
    ]
    for question in simple_questions:
        result = agent.run_sync(question)
        print(f"Q: {question}, result is:\n {result.data}\n")

    """
    complex_questions = [
        'We are small family living in the mountains in the winter cottage. What is best car for us?'
    ]
    for question in complex_questions:
        result = agent.run_sync(question)
        print(f"Q: {question}, result is:\n {result.data}\n")
    """


if __name__ == "__main__":
    main()
