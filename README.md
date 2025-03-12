# **RapidClip**

**RapidClip** is an ongoing project aimed at automating the creation of short videos, ideal for platforms like YouTube Shorts, Instagram Reels, TikTok, and Kwai. The goal is to enable the system to generate complete videos from a provided topic, combining narration, background music, dynamic images, visual effects, synchronized subtitles, detailed process logging, and final video assembly with animated transitions.

🇧🇷 For a Portuguese version of this README, see [README.pt-br.md](README.pt-br.md).

---

## **Implemented Features**

- **Automatic Content Creation**: Generate personalized scripts based on the provided topic.
- **Audio Narration**: Transform the script into high-quality narration, with support for both ElevenLabs and OpenAI TTS.
- **Audio Reprocessing**: Reprocess audio files that exceed a specified duration to ensure compatibility with platform constraints.
- **Subtitle Generation**: Generate subtitles with improved alignment and segmentation:
  - Tokenizes the transcript text while preserving punctuation.
  - Aligns words with their respective timestamps and punctuation.
  - Creates readable, synchronized subtitles with character and word limits per line.
- **Enhanced Image Generation**:
  - Generate diverse image prompts using an OpenAI-based prompt generator that leverages the full subtitle context and previously generated prompts (included only when available), ensuring varied and creative visual outputs.
  - Supports a configurable SANA model version for image generation via Replicate.
- **Video Assembly**: Assemble a final video using the generated audio, images, and subtitles with animated transitions. A dedicated module composes these elements into a final video file with a resolution of 1080x1920.
- **Multi-Language Support**: Enable content creation, narration, and subtitles in multiple languages.
- **Process Logging**: Detailed logs of the overall video generation process, including the generated image prompts, are saved in each video's output folder.

---

## **Planned Features**

- **Background Music Integration**: Select local soundtracks to enrich the video.
- **Relevant Images**: Further refine image selection to better illustrate the content.
- **Visual Effects and Transitions**: Apply zoom, animations, and smooth cuts.
- **Complete Rendering**: Create the final video ready for publication.
- **Additional Video Editing Enhancements**: Expand features for more advanced video composition and editing.

---

## **How to Use**

Before running RapidClip, make sure to configure the required environment variables. Use the `.env.example` file as a template and create a `.env` file with the following variables:

```plaintext
OPENAI_API_KEY=your-openai-api-key
ELEVENLABS_API_KEY=your-elevenlabs-api-key
REPLICATE_API_TOKEN=your-replicate-api-token
SANA_MODEL_VERSION=your-sana-model-version
```

After configuring the environment variables, you can run RapidClip using one of the following commands.

### Example with ElevenLabs TTS

```bash
python src/main.py --theme "Curiosities of History (a single curiosity)" \
  --language "pt-BR" \
  --voice_id "CstacWqMhJQlnfLPxRG4" \
  --max_duration 60 \
  --tts_service elevenlabs
```

### Example with OpenAI TTS

```bash
python src/main.py --theme "Curiosities of Technology (a single curiosity)" \
  --language "en" \
  --max_duration 60 \
  --tts_service openai \
  --openai_tts_model "tts-1-hd" \
  --openai_tts_voice "onyx"
```

### Parameters:
- `--theme`: The theme of the script to be created.
- `--language`: The language for the script and narration.
- `--tts_service`: The TTS service to use (`elevenlabs` or `openai`). Defaults to `elevenlabs`.
- `--voice_id`: The ID of the voice to be used for narration (required for ElevenLabs).
- `--openai_tts_model`: The OpenAI TTS model to use (default: `tts-1-hd`).
- `--openai_tts_voice`: The OpenAI TTS voice to use (default: `alloy`).
- `--max_duration`: The maximum allowed duration for the audio (in seconds).

### Output:
The generated files will be saved in the `output/` folder, including:
- An audio file (`.mp3`) containing the narration.
- A subtitle file (`.srt`) synchronized with the audio.
- A `process.log` file containing detailed logs of the video generation process, including the image prompts generated for each subtitle interval.
- A final video file (`_final.mp4`) assembled with animated transitions.

#### Subtitle Approach:
The subtitle generation process ensures improved alignment and readability:
- **Tokenization with Punctuation**: The complete transcript text is tokenized into words and punctuation, preserving the original order.
- **Word-Punctuation Alignment**: Each word is aligned with its corresponding token, ensuring punctuation is correctly placed.
- **Cue Segmentation**: Subtitles are divided into smaller segments (cues) based on word and character limits per line, maintaining synchronization with audio timestamps.

---

## **Project Status**

**RapidClip** is in its initial development phase. The core functionalities are in place, and recent updates include:
- Enhanced image generation prompts with diversity and process logging.
- Support for a configurable SANA model version.
- Implementation of a video assembly module that combines audio, images, and subtitles with animated transitions to produce a final video at 1080x1920 resolution.

Continuous improvements are being made to ensure an efficient and intuitive workflow.

---

## **Next Steps**

1. Structure the pipeline for creating scripts, narration, and generating images.
2. Implement additional visual effects and transitions between images.
3. Ensure precise synchronization of audio, images, and subtitles.
4. Optimize final rendering to ensure compatibility with short video platforms.
5. Expand support for audio processing, including reprocessing long audio files and handling user-defined duration limits.
6. Enhance video editing capabilities for more advanced features.

---

## **Contributions**

For a Portuguese version of this README, see [README.pt-br.md](README.pt-br.md).

If you'd like to collaborate on the project, follow these steps:

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