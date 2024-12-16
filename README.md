# **RapidClip**

**RapidClip** is an ongoing project aimed at automating the creation of short videos, ideal for platforms like YouTube Shorts, Instagram Reels, TikTok, and Kwai. The goal is to enable the system to generate complete videos from a provided topic, combining narration, background music, dynamic images, visual effects, and synchronized subtitles.

🇧🇷 For a Portuguese version of this README, see [README.pt-br.md](README.pt-br.md).

---

## **Implemented Features**

- **Automatic Content Creation**: Generate personalized scripts based on the provided topic.
- **Audio Narration**: Transform the script into high-quality narration.
- **Audio Reprocessing**: Reprocess audio files that exceed a specified duration to ensure compatibility with platform constraints.
- **Subtitle Generation**: Generate subtitles with improved alignment and segmentation:
  - Tokenizes the transcript text while preserving punctuation.
  - Aligns words with their respective timestamps and punctuation.
  - Creates readable, synchronized subtitles with character and word limits per line.
- **Multi-Language Support**: Enable content creation, narration, and subtitles in multiple languages.

---

## **Planned Features**

- **Background Music Integration**: Select local soundtracks to enrich the video.
- **Relevant Images**: Automatically generate images to illustrate the content.
- **Visual Effects and Transitions**: Apply zoom, animations, and smooth cuts.
- **Complete Rendering**: Create the final video ready for publication.

---

## **Project Status**

**RapidClip** is in its initial development phase. Features are being implemented and tested to ensure an efficient and intuitive workflow.

---

## **Next Steps**

1. Structure the pipeline for creating scripts, narration, and generating images.
2. Implement visual effects and transitions between images.
3. Ensure precise synchronization of audio, images, and subtitles.
4. Optimize final rendering to ensure compatibility with short video platforms.
5. Expand support for audio processing, including reprocessing long audio files and handling user-defined duration limits.

---

## **Contributions**

For a Portuguese version of this README, see [README.pt-br.md](README.pt-br.md).

We welcome contributions! If you'd like to collaborate on the project, follow these steps:

1. Fork the repository.
2. Create a branch for your feature or bug fix:
   ```bash
   git checkout -b my-contribution
   ```
3. Make your changes and submit a pull request detailing your modifications.

We'd love your help to make RapidClip even better!

---

## **License**

This project is licensed under the **MIT** license. This means you are free to use, modify, and distribute it, provided the original license is included in the code. See the [LICENSE](LICENSE) file for more details.