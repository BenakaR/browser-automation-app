# src/backend/browser_agent.py
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
from pydantic import SecretStr
import os
import json

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError('GEMINI_API_KEY is not set')

async def main(task):
    agent = Agent(
        task=task,
        llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=SecretStr(api_key)),
    )
    await agent.run()
    agent.save_history("history.json")
    with open("history.json", "r") as f:
        history = json.loads(f.read())
    if history["history"][-1]["result"] and history["history"][-1]["result"][0]["is_done"] == True:
        return "Success: \n" + history["history"][-1]["result"][0]["extracted_content"]
    return "ERROR: \n" + history["history"][-1]["result"][0]["error"]

if __name__ == "__main__":
    task = "Plan a trip to Paris with 5 friends for the duration of 7 days."
    result = asyncio.run(main(task))
    print(result)