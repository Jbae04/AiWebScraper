from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig, Controller
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
import os
import asyncio
import json

load_dotenv()

# Define the data models
class Post(BaseModel):
    caption: str
    url: str

class Posts(BaseModel):
    posts: List[Post]

# Initialize the controller with the output model
controller = Controller(output_model=Posts)

# Configure the browser
browser = Browser(
    config=BrowserConfig(
        browser_binary_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    )
)

# Retrieve the API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(
    model='gemini-1.5-pro',
    google_api_key=api_key
)

async def main():
    # Define the task with a wait action
    task = """
        Go to https://www.youtube.com
        Search for "AI News"
        Wait for 8 seconds to allow dynamic content to load
        Then extract the top 5 video titles and full YouTube URLs from the search results
        Return them as a list of objects with 'caption' and 'url'
        """

    # Initialize the agent with the task and configurations
    agent = Agent(
        task=task.strip(),
        llm=llm,
        browser=browser,
        controller=controller
    )

    # Run the agent
    result = await agent.run()

    # Retrieve the final result
    raw = result.final_result()

    # Attempt to parse the result as JSON
    try:
        parsed = json.loads(raw)

        if isinstance(parsed, dict):
            for key, value in parsed.items():
                print(f"{key}:")
                if isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            print("  - " + ", ".join(f"{k}: {v}" for k, v in item.items()))
                        else:
                            print(f"  - {item}")
                else:
                    print(f"  {value}")

        elif isinstance(parsed, list):
            for item in parsed:
                if isinstance(item, dict):
                    print("- " + ", ".join(f"{k}: {v}" for k, v in item.items()))
                else:
                    print(f"- {item}")

        else:
            print(parsed)

    except Exception as e:
        print("Could not parse structured output. Showing raw result:")
        print(raw)

    # Close the browser
    await browser.close()

# Execute the main function
asyncio.run(main())
