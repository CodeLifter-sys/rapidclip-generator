from pydantic import BaseModel, ValidationError
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from openai import OpenAI
import json


class MusicChoiceResponse(BaseModel):
    reasoning: str
    id: int


class OpenAIService:
    """
    Service to interact with the OpenAI API for generating video scripts, image prompts,
    and selecting appropriate background music.
    """

    def __init__(self, api_key: str):
        """
        Initialize the service with the provided API key.

        Args:
            api_key (str): OpenAI API key.
        """
        model = OpenAIModel('gpt-4o', api_key=api_key)
        self.agent = Agent(model)
        self.openai_client = OpenAI(api_key=api_key)

    def generate_script(self, theme: str, language: str) -> str:
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

    def generate_image_prompt(
        self, full_subtitles: str, previous_prompts: list, group_text: str
    ) -> str:
        """
        Generate a prompt for image generation based on subtitle context.

        Args:
            full_subtitles (str): The entire subtitle text for context.
            previous_prompts (list): List of previously generated image prompts.
            group_text (str): The specific subtitle segment to create an image prompt for.

        Returns:
            str: The generated image prompt in English.
        """
        prompt = (
            "You are a creative prompt generator for text-to-image models. "
            "Your task is to generate a concise and descriptive prompt in English for generating an artistic image that visually represents a given context. "
            "Ensure that your generated prompt is diverse and significantly different from any previously generated prompts. "
            "Use creative and varied language to depict the scene uniquely.\n\n"
            f"1. The entire subtitle context:\n{full_subtitles}\n\n"
        )
        if previous_prompts:
            prompt += f"2. Previously generated prompts:\n{previous_prompts}\n\n"

        prompt += (
            f"3. Subtitle segment to illustrate:\n{group_text}\n\n"
            "Based on this information, generate a creative and concise prompt in English."
        )
        result = self.agent.run_sync(prompt)
        return result.data

    def generate_music_choice(
        self, script: str, image_prompts: list, songs_json: str
    ) -> MusicChoiceResponse:
        """
        Generate a background music choice based on the video script, image prompts, and available songs.

        Args:
            script (str): The video script.
            image_prompts (list): Generated image prompts for the video.
            songs_json (str): JSON representation of available songs.

        Returns:
            MusicChoiceResponse: Object containing the reasoning and the ID of the chosen song.
        """
        prompt = (
            "You are a creative assistant for selecting background music for videos. "
            "Based on the script below, the already generated image prompts, and the list of available songs, "
            "choose the music that best fits as background music for the video. "
            "The available songs list is provided in JSON format and contains objects with the keys 'id', 'file', 'keywords', 'artist', and 'source'.\n\n"
            f"Script:\n{script}\n\n"
            f"Image Prompts:\n{image_prompts}\n\n"
            f"Songs List (JSON):\n{songs_json}\n\n"
            "Respond ONLY with a valid JSON object following this schema:\n"
            '{ "reasoning": "(reason for choosing the music)", "id": (id of the chosen song) }'
        )

        # Força o retorno em JSON via response_format={"type": "json_object"}
        completion = self.openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
        )

        # Extraímos a primeira escolha
        choice = completion.choices[0]

        # O valor pode já vir como dict ou como string. Tratamos ambos os casos.
        response_data = choice.message.content

        # Se for dict, ótimo. Se for string, tentamos json.loads().
        if isinstance(response_data, dict):
            result_data = response_data
        elif isinstance(response_data, str):
            try:
                result_data = json.loads(response_data)
            except json.JSONDecodeError as e:
                raise ValueError(
                    f"Could not decode JSON from the model response:\n{response_data}\n\nError: {e}"
                )
        elif hasattr(response_data, "to_dict"):
            result_data = response_data.to_dict()
        else:
            raise ValueError(
                f"Unexpected response type for message content: {type(response_data)}"
            )

        return MusicChoiceResponse(**result_data)
