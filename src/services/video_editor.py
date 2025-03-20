from moviepy import (
    AudioFileClip,
    ImageClip,
    CompositeVideoClip,
    TextClip,
    CompositeAudioClip,
    concatenate_audioclips
)
from moviepy.video.fx import FadeIn, FadeOut, Resize
from moviepy.audio.fx import MultiplyVolume
from moviepy.video.tools.subtitles import SubtitlesClip
import numpy as np
import os


def make_textclip(txt):
    """
    Creates a TextClip for subtitles.

    Args:
        txt (str): The subtitle text.

    Returns:
        TextClip: The formatted text clip.
    """
    return TextClip(
        text=txt,
        font="fonts/Helvetica.ttf",
        font_size=50,
        color="yellow",
        stroke_color="black",
        stroke_width=2,
        method="caption",
        size=(1000, None)
    )


def assemble_video(video_folder, file_id, cues, background_music_path=None):
    """
    Assembles a final video by combining narration audio, images, subtitles, and background music.

    Args:
        video_folder (str): The directory where video assets are stored.
        file_id (str): The unique identifier for the video.
        cues (list): Subtitle cues defining the timing of text overlays.
        background_music_path (str, optional): Path to the background music file. Defaults to None.

    Returns:
        str: The path to the final video file.
    """

    # Load narration audio
    audio_path = os.path.join(video_folder, f"{file_id}.mp3")
    narration_audio = AudioFileClip(audio_path)
    video_duration = narration_audio.duration

    # Process background music if provided
    if background_music_path:
        bg_music = AudioFileClip(background_music_path)

        # Loop background music if its duration is shorter than the narration
        if bg_music.duration < video_duration:
            loops = int(video_duration // bg_music.duration) + 1
            bg_music = concatenate_audioclips([bg_music] * loops)

        # Trim background music to match the narration duration
        if bg_music.duration > video_duration:
            bg_music = bg_music.with_duration(video_duration)

        # Reduce background music volume
        bg_music = bg_music.with_effects([MultiplyVolume(0.2)])

        # Combine narration with background music
        combined_audio = CompositeAudioClip([narration_audio, bg_music])
    else:
        combined_audio = narration_audio

    # Create the base video with zoom effect on the first image
    first_image = os.path.join(video_folder, f"{file_id}_img_1.png")
    background = ImageClip(first_image).with_duration(video_duration)
    background = background.with_effects([Resize(lambda t: 1 + 0.02 * t)])

    # Add additional images with transitions
    image_clips = []
    # Number of images based on subtitle groups
    num_images = (len(cues) + 1) // 2
    for i in range(1, num_images):
        group = cues[i*2:i*2+2]
        start = group[0][0]
        end = group[-1][1]
        duration = end - start

        img_path = os.path.join(video_folder, f"{file_id}_img_{i+1}.png")
        clip = ImageClip(img_path).with_duration(duration)
        clip = clip.with_start(start)
        clip = clip.with_effects([
            FadeIn(0.5),
            FadeOut(0.5),
            Resize(lambda t: 1 + 0.02 * t)
        ])
        image_clips.append(clip)

    # Create the final video composition with images and transitions
    video = CompositeVideoClip([background] + image_clips, size=(1080, 1920))

    # Add subtitles
    srt_path = os.path.join(video_folder, f"{file_id}.srt")
    subtitles = SubtitlesClip(
        subtitles=srt_path, make_textclip=make_textclip).with_position(("center", 1620))

    # Merge all elements together
    final = CompositeVideoClip([video, subtitles], size=(1080, 1920))
    final = final.with_audio(combined_audio)
    final = final.with_duration(video_duration)

    # Export the final video
    output_path = os.path.join(video_folder, f"{file_id}_final.mp4")
    final.write_videofile(output_path, fps=24)

    return output_path
