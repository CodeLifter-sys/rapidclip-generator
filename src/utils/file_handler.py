import os
import uuid
from PIL import Image, ImageDraw, ImageFont


def get_font(font_size):
    """
    Attempts to load a scalable TrueType font.
    Falls back to the default font if none are found (non-scalable).
    """
    for font_name in ("arial.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(font_name, font_size)
        except IOError:
            continue
    print("Warning: No scalable TrueType font found. Using non-scalable default font.")
    return ImageFont.load_default()


def apply_watermark(image, watermark_text, margin=0.9):
    """
    Applies a textual watermark to the image. 
    Scales the font so the text fills most of the image width.

    :param image: PIL.Image object to be modified.
    :param watermark_text: Text to use as watermark.
    :param margin: A float from 0 to 1 indicating the max width percentage for the watermark.
    :return: Watermarked image as a new PIL.Image object.
    """
    image = image.convert("RGBA")
    txt_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)

    # Base font size to measure initial text width
    base_font_size = 100
    base_font = get_font(base_font_size)
    available_width = image.width * margin

    # Measure text width using base font
    bbox = draw.textbbox((0, 0), watermark_text, font=base_font)
    base_text_width = bbox[2] - bbox[0]

    # Calculate scale factor and determine new font size
    scale_factor = available_width / base_text_width if base_text_width else 1
    new_font_size = int(base_font_size * scale_factor)
    font = get_font(new_font_size)

    # Re-measure text dimensions with new font
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Center text on the image
    text_position = ((image.width - text_width) / 2,
                     (image.height - text_height) / 2)

    # Draw watermark text with semi-transparency
    draw.text(text_position, watermark_text,
              font=font, fill=(255, 255, 255, 128))

    # Combine watermark layer with the original image
    watermarked = Image.alpha_composite(image, txt_layer)
    return watermarked.convert("RGB")


def save_audio(response, directory="output", file_id=None):
    """
    Saves audio data to a file.

    :param response: The audio data to save (bytes).
    :param directory: The directory where the audio file will be saved.
    :param file_id: An optional unique identifier to name the file.
    :return: Path to the saved audio file.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    if not file_id:
        file_id = str(uuid.uuid4())

    output_file = f"{directory}/{file_id}.mp3"

    with open(output_file, "wb") as f:
        f.write(response)

    return output_file


def save_subtitles(srt_content, directory="output", file_id=None):
    """
    Saves subtitle data to an SRT file.

    :param srt_content: The subtitle content.
    :param directory: The directory where the SRT file will be saved.
    :param file_id: An optional unique identifier to name the file.
    :return: Path to the saved SRT file.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    if not file_id:
        file_id = str(uuid.uuid4())

    subtitle_file = f"{directory}/{file_id}.srt"

    with open(subtitle_file, "w", encoding="utf-8") as f:
        f.write(srt_content)

    return subtitle_file


def save_image(image_data, directory="output", file_id=None, suffix="image", watermark=None):
    """
    Saves image bytes to a PNG file and optionally applies a watermark.

    :param image_data: Image data (bytes).
    :param directory: Directory where the image will be saved.
    :param file_id: Optional custom identifier for the file name.
    :param suffix: Suffix to append to the filename (before the extension).
    :param watermark: Optional text to use as a watermark.
    :return: Path to the saved image file.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    if not file_id:
        file_id = str(uuid.uuid4())

    output_file = f"{directory}/{file_id}_{suffix}.png"

    # Save raw image data
    with open(output_file, "wb") as f:
        f.write(image_data)

    # Apply watermark if provided
    if watermark:
        image = Image.open(output_file)
        watermarked_image = apply_watermark(image, watermark)
        watermarked_image.save(output_file, "PNG")

    return output_file
