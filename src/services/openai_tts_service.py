from openai import OpenAI
from io import BytesIO
import tempfile
import os


class OpenAITTSService:
    """
    Service to interact with the OpenAI API for text-to-speech conversion.
    """

    def __init__(self, api_key):
        """
        Initialize the service with the API key.

        Args:
            api_key (str): OpenAI API key.
        """
        self.client = OpenAI(api_key=api_key)

    def text_to_speech(self, text, model="tts-1-hd", voice="alloy"):
        """
        Convert text to speech using the specified model and voice.

        Args:
            text (str): The text to convert.
            model (str): The OpenAI TTS model to use (default: "tts-1-hd").
            voice (str): The OpenAI TTS voice to use (default: "alloy").

        Returns:
            bytes: The raw audio data in MP3 format.
        """
        response = self.client.audio.speech.create(
            model=model,
            voice=voice,
            input=text,
        )

        # Cria um arquivo temporário para gravar a saída do stream
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
            tmp_file_path = tmp_file.name

        # Usa o caminho temporário para salvar a resposta
        response.stream_to_file(tmp_file_path)

        try:
            # Lê o conteúdo do arquivo temporário em memória
            with open(tmp_file_path, "rb") as f:
                audio_data = f.read()
        finally:
            # Remove o arquivo temporário
            os.remove(tmp_file_path)

        return audio_data
