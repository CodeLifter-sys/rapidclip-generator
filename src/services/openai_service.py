from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel


class OpenAIService:
    def __init__(self, api_key):
        model = OpenAIModel('gpt-4o', api_key=api_key)
        self.agent = Agent(model)

    def generate_script(self, theme, language):
        prompt = (
            f"You are a scriptwriter specializing in creating short scripts for videos up to 60 seconds, such as "
            f"YouTube Shorts, Reels, and TikTok. Create an engaging, informative, and concise script for the following theme: "
            f"'{theme}'. Provide only the narration text without any scene directions or additional notes. The script should be in {
                language}."
        )
        result = self.agent.run_sync(prompt)
        return result.data
