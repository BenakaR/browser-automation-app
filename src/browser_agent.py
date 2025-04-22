# src/backend/browser_agent.py
from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio
from dotenv import load_dotenv
from pydantic import SecretStr
import os
import json

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError('GEMINI_API_KEY is not set')

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext
from browser_use.agent.views import ActionResult
import logging

logger = logging.getLogger(__name__)
controller = Controller()

@controller.action('Upload file to interactive element with file path')
async def upload_file(index: int, path: str, browser: BrowserContext):
    if not os.path.exists(path):
        return ActionResult(error=f'File {path} does not exist')
    try:
        page = await browser.get_current_page()
        file_input = page.locator('input[type="file"]')
        if not file_input:
            msg = f'No file input element found at index {index}'
            logger.info(msg)
            return ActionResult(error=msg)
        absolute_path = os.path.abspath(path)
        await file_input.set_input_files(absolute_path)
        return ActionResult(extracted_content=f"Document uploaded: {path}", include_in_memory=True)
    except Exception as e:
        msg = f'Failed to upload file to index {index}: {str(e)}'
        logger.info(msg)
        return ActionResult(error=msg)

# @controller.action(
# 	'Upload file to interactive element with file path ',
# )
# async def upload_file(index: int, path: str, browser: BrowserContext):

# 	if not os.path.exists(path):
# 		return ActionResult(error=f'File {path} does not exist')

# 	dom_el = await browser.get_dom_element_by_index(index)

# 	file_upload_dom_el = dom_el.get_file_upload_element()

# 	if file_upload_dom_el is None:
# 		msg = f'No file upload element found at index {index}!!!'
# 		logger.info(msg)
# 		return ActionResult(error=msg)

# 	file_upload_el = await browser.get_locate_element(file_upload_dom_el)

# 	if file_upload_el is None:
# 		msg = f'No file upload element found at index {index}'
# 		logger.info(msg)
# 		return ActionResult(error=msg)

# 	try:
# 		await file_upload_el.set_input_files(path)
# 		msg = f'Successfully uploaded file to index {index}'
# 		logger.info(msg)
# 		return ActionResult(extracted_content=msg, include_in_memory=True)
# 	except Exception as e:
# 		msg = f'Failed to upload file to index {index}: {str(e)}'
# 		logger.info(msg)
# 		return ActionResult(error=msg)

async def main(task: str):
    browser = Browser(
        config=BrowserConfig(
            chrome_instance_path="C://Program Files/Google/Chrome/Application/chrome.exe",
        ),
    )

    data = {
        "email": os.getenv("EMAIL"),
        "password": os.getenv("PASSWORD"),
    }
    available_file_paths = [
        "E:\\IgniteIQ\\browser-automation-app\\requirements.txt",
    ]
    agent = Agent(
        task=task+"\n Use the upload_file action to upload files.",
        browser=browser,
        llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=SecretStr(api_key)),
        # planner_llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash', api_key=SecretStr(api_key)),
        controller=controller,
        sensitive_data=data,
        available_file_paths=available_file_paths,
        generate_gif=True,
    )
    await agent.run()
    # agent.save_history("history.json")
    # with open("history.json", "r") as f:
    #     history = json.loads(f.read())
    # if history["history"][-1]["result"] and history["history"][-1]["result"][0]["is_done"] == True:
    #     return "Success: \n" + history["history"][-1]["result"][0]["extracted_content"]
    # return "ERROR: \n" + history["history"][-1]["result"][0]["error"]

if __name__ == "__main__":
    task = "Plan a trip to Paris with 5 friends for the duration of 7 days."
    result = asyncio.run(main(task))
    print(result)