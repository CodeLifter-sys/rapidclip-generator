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
    """Gera um TextClip para uma legenda"""
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
    # Carrega áudio de narração
    audio_path = os.path.join(video_folder, f"{file_id}.mp3")
    narration_audio = AudioFileClip(audio_path)
    video_duration = narration_audio.duration

    # Processa música de fundo
    if background_music_path:
        bg_music = AudioFileClip(background_music_path)

        # Loop se necessário
        if bg_music.duration < video_duration:
            loops = int(video_duration // bg_music.duration) + 1
            bg_music = concatenate_audioclips([bg_music] * loops)

        # Trunca para duração do vídeo
        if bg_music.duration > video_duration:
            bg_music = bg_music.with_duration(video_duration)

        # Reduz volume
        bg_music = bg_music.with_effects([MultiplyVolume(0.2)])

        # Combina com narração
        combined_audio = CompositeAudioClip([narration_audio, bg_music])
    else:
        combined_audio = narration_audio

    # Monta vídeo base com zoom
    first_image = os.path.join(video_folder, f"{file_id}_img_1.png")
    background = ImageClip(first_image).with_duration(video_duration)
    background = background.with_effects([Resize(lambda t: 1 + 0.02 * t)])

    # Adiciona outras imagens
    image_clips = []
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

    # Composição final
    video = CompositeVideoClip([background] + image_clips, size=(1080, 1920))

    # Adiciona legendas
    srt_path = os.path.join(video_folder, f"{file_id}.srt")
    subtitles = SubtitlesClip(
        subtitles=srt_path, make_textclip=make_textclip).with_position(("center", 1620))

    # Junta tudo
    final = CompositeVideoClip([video, subtitles], size=(1080, 1920))
    final = final.with_audio(combined_audio)
    final = final.with_duration(video_duration)

    # Exporta
    output_path = os.path.join(video_folder, f"{file_id}_final.mp4")
    final.write_videofile(output_path, fps=24)

    return output_path
