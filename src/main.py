from config.settings import OPENAI_API_KEY, ELEVENLABS_API_KEY
from parsers.arguments import parse_args
from services.openai_service import OpenAIService
from services.elevenlabs_service import ElevenLabsService
from utils.file_handler import save_audio
from utils.logger import setup_logger
from utils.audio_processing import reprocess_audio
import os
import sys


def main():
    """
    Main entry point for the application.
    - Generates a script using OpenAI API.
    - Converts the script to speech using Eleven Labs API.
    - Processes the audio if max_duration is specified.
    """
    logger = setup_logger()
    args = parse_args()

    # Initialize services
    logger.info("Initializing services...")
    openai_service = OpenAIService(api_key=OPENAI_API_KEY)
    elevenlabs_service = ElevenLabsService(api_key=ELEVENLABS_API_KEY)

    # Generate the script
    logger.info("Generating script with OpenAI...")
    try:
        script_text = openai_service.generate_script(
            theme=args.theme, language=args.language)
        logger.debug(f"Generated script: {script_text}")
    except Exception as e:
        logger.error(f"Error generating script: {e}")
        sys.exit(1)

    # Convert script to audio
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
        sys.exit(1)

    # Process audio if max_duration is provided
    if args.max_duration:
        logger.info(f"Processing audio to ensure it does not exceed {
                    args.max_duration} seconds...")
        try:
            # Read the original audio file as bytes
            with open(output_file, 'rb') as f:
                audio_bytes = f.read()

            # Reprocess the audio (e.g., speed up) if necessary
            processed_bytes = reprocess_audio(
                audio_data=audio_bytes,
                max_duration=args.max_duration,
                logger=logger  # Pass logger for logging within reprocessing
            )

            if processed_bytes != audio_bytes:
                # Overwrite the original file with processed audio
                with open(output_file, 'wb') as f:
                    f.write(processed_bytes)
                logger.info(f"Audio processed successfully and saved as {
                            output_file}.")
                logger.debug(f"Original audio file {
                             output_file} overwritten after processing.")
            else:
                # If no processing was needed, keep the original file
                logger.info(
                    "Audio duration is within the maximum duration. No processing needed.")

        except Exception as e:
            logger.error(f"Error processing audio: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
