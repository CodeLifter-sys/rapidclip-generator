import os
import uuid


def save_audio(response, directory="output"):
    if not os.path.exists(directory):
        os.makedirs(directory)
    output_file = f"{directory}/{uuid.uuid4()}.mp3"
    with open(output_file, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)
    return output_file
