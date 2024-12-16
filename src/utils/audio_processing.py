from pydub import AudioSegment
from io import BytesIO


def reprocess_audio(audio_data: bytes,
                    max_duration: float = None,
                    speedup_chunk: int = 150,
                    speedup_crossfade: int = 25,
                    target_bitrate: str = "320k",
                    logger=None) -> bytes:
    """
    Reprocess the audio to optionally adjust duration and export with a specified bitrate.

    Args:
        audio_data (bytes): The original audio data in bytes format.
        max_duration (float, optional): Maximum allowed duration in seconds. If provided and
                                        the audio exceeds this duration, it will be sped up.
        speedup_chunk (int): Chunk size parameter for the speedup function.
        speedup_crossfade (int): Crossfade parameter for smoothing transitions in speedup.
        target_bitrate (str): Desired MP3 bitrate (e.g., "320k" for higher quality).
        logger: Logger instance for logging.

    Returns:
        bytes: The processed audio data in MP3 format.
    """
    # Load the audio from the byte stream
    audio = AudioSegment.from_file(BytesIO(audio_data), format="mp3")

    # If max_duration is defined, check the duration and speed up if necessary
    if max_duration is not None:
        # Convert milliseconds to seconds
        current_duration = len(audio) / 1000.0
        if current_duration > max_duration:
            speed_factor = current_duration / max_duration
            if logger:
                logger.info(f"Current duration {current_duration} exceeds max duration {max_duration}. "
                            f"Speeding up by a factor of {speed_factor}.")
            # Adjust playback speed with chunking and crossfade for smoother transitions
            audio = audio.speedup(
                playback_speed=speed_factor,
                chunk_size=speedup_chunk,
                crossfade=speedup_crossfade
            )
        else:
            # If no processing is needed, return the original data
            return audio_data

    # Re-export the audio with the specified bitrate
    output_data = BytesIO()
    audio.export(output_data, format="mp3",
                 parameters=["-b:a", target_bitrate])
    output_data.seek(0)

    return output_data.read()
