from elevenlabs import ElevenLabs, VoiceSettings


class ElevenLabsService:
    def __init__(self, api_key):
        self.client = ElevenLabs(api_key=api_key)

    def text_to_speech(self, voice_id, text, stability=0.75, similarity_boost=0.85):
        response = self.client.text_to_speech.convert(
            voice_id=voice_id,
            output_format="mp3_44100_128",
            text=text,
            model_id="eleven_multilingual_v2",
            voice_settings=VoiceSettings(
                stability=stability,
                similarity_boost=similarity_boost
            )
        )
        return response
