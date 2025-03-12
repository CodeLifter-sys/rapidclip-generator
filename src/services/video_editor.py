from moviepy import AudioFileClip, ImageClip, CompositeVideoClip, TextClip, ColorClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.fx.FadeIn import FadeIn
from moviepy.video.fx.FadeOut import FadeOut
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
        # Caminho para a fonte que você adicionará na pasta 'fonts' do projeto
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

    # Create a black background clip for the entire duration
    background = ColorClip(size=(1080, 1920), color=(
        0, 0, 0), duration=video_duration)

    # Create image clips based on cues. Each image corresponds to up to two cues.
    image_clips = []
    num_images = (len(cues) + 1) // 2
    for i in range(num_images):
        group_cues = cues[i * 2: i * 2 + 2]
        start_time = group_cues[0][0]
        end_time = group_cues[-1][1]
        duration = end_time - start_time
        image_path = os.path.join(video_folder, f"{file_id}_img_{i + 1}.png")
        clip = ImageClip(image_path).with_duration(duration)
        clip = clip.with_start(start_time).with_effects(
            [FadeIn(0.5), FadeOut(0.5)])
        image_clips.append(clip)

    video = CompositeVideoClip([background] + image_clips, size=(1080, 1920))

    # Generate subtitles using SubtitlesClip with the make_textclip function.
    srt_path = os.path.join(video_folder, f"{file_id}.srt")
    subtitles = SubtitlesClip(
        subtitles=srt_path, make_textclip=make_textclip).with_position(("center", 1620))

    final_video = CompositeVideoClip([video, subtitles], size=(1080, 1920))
    final_video = final_video.with_audio(audio_clip)
    final_video = final_video.with_duration(video_duration)

    output_path = os.path.join(video_folder, f"{file_id}_final.mp4")
    final_video.write_videofile(output_path, fps=24)

    return output_path
