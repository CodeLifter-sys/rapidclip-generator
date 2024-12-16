from config.settings import OPENAI_API_KEY, ELEVENLABS_API_KEY
from parsers.arguments import parse_args
from services.openai_service import OpenAIService
from services.elevenlabs_service import ElevenLabsService
from utils.file_handler import save_audio
from utils.logger import setup_logger


def main():
    logger = setup_logger()
    args = parse_args()

    logger.info("Initializing services...")
    openai_service = OpenAIService(api_key=OPENAI_API_KEY)
    elevenlabs_service = ElevenLabsService(api_key=ELEVENLABS_API_KEY)

    logger.info("Generating script with OpenAI...")
    try:
        script_text = openai_service.generate_script(
            theme=args.theme, language=args.language)
        logger.debug(f"Generated script: {script_text}")
    except Exception as e:
        logger.error(f"Error generating script: {e}")
        exit(1)

    logger.info("Converting text to speech with Eleven Labs...")
    try:
        response = elevenlabs_service.text_to_speech(
            voice_id=args.voice_id,
            text=script_text,
            stability=args.stability,
            similarity_boost=args.similarity_boost
        )
        output_file = save_audio(response)
        logger.info(f"Audio successfully generated and saved as {
                    output_file}.")
    except Exception as e:
        logger.error(f"Error generating audio: {e}")
        exit(1)


if __name__ == "__main__":
    main()
