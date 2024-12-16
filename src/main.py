import sys
import uuid
from config.settings import OPENAI_API_KEY, ELEVENLABS_API_KEY
from parsers.arguments import parse_args
from services.openai_service import OpenAIService
from services.elevenlabs_service import ElevenLabsService
from services.whisper_service import WhisperService
from utils.file_handler import save_audio, save_subtitles
from utils.logger import setup_logger
from utils.audio_processing import reprocess_audio
from utils.subtitle_handler import align_words_with_punctuation, format_srt_from_aligned_words


def main():
    """
    Main entry point for the application.
    - Generates a script using OpenAI API.
    - Converts the script to speech using Eleven Labs API.
    - Processes the audio if max_duration is specified.
    - Generates subtitles from the audio using OpenAI's Whisper API.
    """
    logger = setup_logger()
    args = parse_args()

    # Initialize services
    logger.info("Initializing services...")
    openai_service = OpenAIService(api_key=OPENAI_API_KEY)
    elevenlabs_service = ElevenLabsService(api_key=ELEVENLABS_API_KEY)
    whisper_service = WhisperService(api_key=OPENAI_API_KEY)

    # Generate the script
    logger.info("Generating script with OpenAI...")
    try:
        script_text = openai_service.generate_script(
            theme=args.theme, language=args.language
        )
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

        # Generate a single file_id for both audio and subtitles
        file_id = str(uuid.uuid4())
        output_file = save_audio(response, file_id=file_id)
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
                logger=logger
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

    # Generate subtitles from audio
    logger.info("Generating subtitles with Whisper...")
    try:
        transcript = whisper_service.transcribe_audio(
            audio_file_path=output_file)
        aligned_words = align_words_with_punctuation(
            transcript.words, transcript.text)
        srt_content = format_srt_from_aligned_words(aligned_words)
        subtitle_file = save_subtitles(srt_content, file_id=file_id)
        logger.info(f"Subtitles generated and saved as {subtitle_file}.")
    except Exception as e:
        logger.error(f"Error generating subtitles: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
