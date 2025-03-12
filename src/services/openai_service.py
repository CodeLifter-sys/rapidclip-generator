from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel


class OpenAIService:
    """
    Service to interact with the OpenAI API for generating video scripts.
    """

    def __init__(self, api_key):
        """
        Initialize the service with the API key.

        Args:
            api_key (str): OpenAI API key.
        """
        model = OpenAIModel('gpt-4o', api_key=api_key)
        self.agent = Agent(model)

    def generate_script(self, theme, language):
        """
        Generate a short script for a video based on the theme and language.

        Args:
            theme (str): The subject of the script.
            language (str): The language in which the script is written.

        Returns:
            str: The generated script.
        """
        prompt = (
            f"You are a scriptwriter specializing in creating short scripts for videos up to 60 seconds, such as "
            f"YouTube Shorts, Reels, and TikTok. Create an engaging, informative, and concise script for the following theme: "
            f"'{theme}'. Provide only the narration text without any scene directions or additional notes. The script should be in {language}."
        )
        result = self.agent.run_sync(prompt)
        return result.data


class OpenAIService:
    """
    Service to interact with the OpenAI API for generating video scripts and image prompts.
    """

    def __init__(self, api_key):
        """
        Initialize the service with the API key.

        Args:
            api_key (str): OpenAI API key.
        """
        model = OpenAIModel('gpt-4o', api_key=api_key)
        self.agent = Agent(model)

    def generate_script(self, theme, language):
        """
        Generate a short script for a video based on the theme and language.

        Args:
            theme (str): The subject of the script.
            language (str): The language in which the script is written.

        Returns:
            str: The generated script.
        """
        prompt = (
            f"You are a scriptwriter specializing in creating short scripts for videos up to 60 seconds, such as "
            f"YouTube Shorts, Reels, and TikTok. Create an engaging, informative, and concise script for the following theme: "
            f"'{theme}'. Provide only the narration text without any scene directions or additional notes. The script should be in {language}."
        )
        result = self.agent.run_sync(prompt)
        return result.data

    def generate_image_prompt(self, full_subtitles, previous_prompts, group_text):
        """
        Generate a prompt for image generation based on the subtitle context.

        Args:
            full_subtitles (str): The entire subtitle text for context.
            previous_prompts (list): List of image prompts generated previously for the same video.
            group_text (str): The specific subtitle segment for which to generate an image prompt.

        Returns:
            str: The generated image prompt in English.
        """
        prompt = (
            "You are a creative prompt generator for text-to-image models. "
            "Your task is to generate a concise and descriptive prompt in English for generating an artistic image that visually represents a given context. "
            "Ensure that your generated prompt is diverse and significantly different from any previously generated prompts. "
            "Use creative and varied language to depict the scene uniquely.\n\n"
            "1. The entire subtitle context:\n"
            f"{full_subtitles}\n\n"
        )
        if previous_prompts:
            prompt += (
                "2. A list of prompts of images generated previously for this video (if any):\n"
                f"{previous_prompts}\n\n"
            )
        prompt += (
            "3. The specific subtitle segment for which to generate an image prompt:\n"
            f"{group_text}\n\n"
            "Based on this information, generate a creative and concise prompt in English."
        )
        result = self.agent.run_sync(prompt)
        return result.data
