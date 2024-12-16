import os
import uuid


def save_audio(response, directory="output"):
    """
    Saves audio data to a file.

    :param response: The audio data to save (bytes).
    :param directory: The directory where the audio file will be saved.
    :return: Path to the saved audio file.
    """
    # Ensure the output directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate a unique file name for the audio file
    output_file = f"{directory}/{uuid.uuid4()}.mp3"

    # Write the audio data to the file directly
    with open(output_file, "wb") as f:
        f.write(response)

    return output_file
