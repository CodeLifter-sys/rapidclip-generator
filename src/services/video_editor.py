from moviepy import AudioFileClip, ImageClip, CompositeVideoClip, TextClip, ColorClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.fx.FadeIn import FadeIn
from moviepy.video.fx.FadeOut import FadeOut
from moviepy.video.fx.Resize import Resize
import os


def make_textclip(txt):
    """
    Generate a TextClip for a subtitle line.

    Args:
        txt (str): The subtitle text.

    Returns:
        TextClip: A TextClip object with the subtitle rendered.
    """
    return TextClip(
        text=txt,
        # Caminho para a fonte que você adicionará na pasta 'fonts' do projeto.
        # Certifique-se de que o arquivo "Helvetica.ttf" (ou outra fonte de sua preferência) esteja na pasta "fonts".
        font="fonts/Helvetica.ttf",
        font_size=50,
        color="yellow",
        stroke_color="black",
        stroke_width=2,
        method="caption",
        size=(1000, None)
    )


def assemble_video(video_folder, file_id, cues):
    """
    Assemble the final video using generated audio, images, and subtitles with animated transitions.
    The video resolution will be 1080x1920.

    Args:
        video_folder (str): The folder where video assets are saved.
        file_id (str): Unique identifier for the video.
        cues (list): A list of subtitle cues as tuples (start, end, text).

    Returns:
        str: The path to the final video file.
    """
    # Load the audio clip
    audio_path = os.path.join(video_folder, f"{file_id}.mp3")
    audio_clip = AudioFileClip(audio_path)
    video_duration = audio_clip.duration

    # Use the first image as the background for the entire video
    first_image_path = os.path.join(video_folder, f"{file_id}_img_1.png")
    background = ImageClip(first_image_path).with_duration(video_duration)
    # Apply a slow zoom in effect on the background image using Resize directly
    background = background.with_effects([Resize(lambda t: 1 + 0.02 * t)])

    # Create image clips for subsequent images (if any)
    image_clips = []
    num_images = (len(cues) + 1) // 2
    # Skip the first image, which is used as background.
    for i in range(1, num_images):
        group_cues = cues[i * 2: i * 2 + 2]
        start_time = group_cues[0][0]
        end_time = group_cues[-1][1]
        duration = end_time - start_time
        image_path = os.path.join(video_folder, f"{file_id}_img_{i + 1}.png")
        clip = ImageClip(image_path).with_duration(duration)
        clip = clip.with_start(start_time)
        clip = clip.with_effects([FadeIn(0.5), FadeOut(0.5)])
        # Apply a slow zoom in effect on the clip using Resize directly
        clip = clip.with_effects([Resize(lambda t: 1 + 0.02 * t)])
        image_clips.append(clip)

    # Composite the video: overlay image clips on the background
    video = CompositeVideoClip([background] + image_clips, size=(1080, 1920))

    # Generate subtitles using SubtitlesClip with the make_textclip function.
    srt_path = os.path.join(video_folder, f"{file_id}.srt")
    subtitles = SubtitlesClip(
        subtitles=srt_path, make_textclip=make_textclip).with_position(("center", 1620))

    # Composite video with subtitles
    final_video = CompositeVideoClip([video, subtitles], size=(1080, 1920))
    final_video = final_video.with_audio(audio_clip)
    final_video = final_video.with_duration(video_duration)

    # Write the final video to file with resolution 1080x1920
    output_path = os.path.join(video_folder, f"{file_id}_final.mp4")
    final_video.write_videofile(output_path, fps=24)

    return output_path
