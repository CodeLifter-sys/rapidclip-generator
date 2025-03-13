# **RapidClip**

**RapidClip** is a project that automates the creation of short videos, ideal for platforms such as YouTube Shorts, Instagram Reels, TikTok, and Kwai. The current version allows you to generate complete videos from a given topic by combining narration, dynamic images, visual effects, synchronized subtitles, detailed process logging, and final video assembly with animated transitions.

🇧🇷 For the Portuguese version of this README, see [README.pt-br.md](README.pt-br.md).

---

## **Implemented Features**

- **Automatic Content Creation**: Personalized script generation based on the provided topic.
- **Audio Narration**: Transformation of the script into high-quality narration, with support for both ElevenLabs and OpenAI TTS.
- **Audio Reprocessing**: Reprocessing of audio that exceeds a specified duration, ensuring compatibility with platform restrictions.
- **Subtitle Generation**: Creation of subtitles with improved alignment and segmentation:
  - Tokenization of the full transcribed text while preserving punctuation.
  - Alignment of words with their corresponding timestamps and punctuation.
  - Generation of legible and synchronized subtitles with character and word limits per line.
- **Enhanced Image Generation**:
  - Generation of diversified prompts for image creation, utilizing the full subtitle context and previously generated prompts (when available) to ensure varied and creative visual outputs.
  - Support for configuring the SANA model version via an environment variable.
- **Final Video Assembly**: Composition of the final video using the generated audio, images, and subtitles, with animated transitions (including a zoom-in effect) and a resolution of 1080x1920.
- **Relevant Images**: Improved selection of images to better illustrate the content.
- **Visual Effects and Transitions**: Application of zoom, animations, and additional smooth cuts.
- **Complete Rendering**: Creation of the final video ready for publication.
- **Multi-Language Support**: The ability to create content, narration, and subtitles in multiple languages.
- **Process Logging**: Storage of detailed logs of the entire process – including the prompts generated for each image interval – in each video’s output folder.

---

## **Planned Features**

- **Background Music Integration**: Selection of local soundtracks to enhance the video.
- **Advanced Video Editing Features**: Expansion of editing capabilities for more advanced functionalities.

---

## **How to Use**

Before running RapidClip, ensure that the required environment variables are set. Use the `.env.example` file as a template and create a `.env` file with the following variables:

```plaintext
OPENAI_API_KEY=your-openai-api-key
ELEVENLABS_API_KEY=your-elevenlabs-api-key
REPLICATE_API_TOKEN=your-replicate-api-token
SANA_MODEL_VERSION=your-sana-model-version
```

After setting the variables, you can run RapidClip using one of the commands below.

### Example with ElevenLabs TTS

```bash
python src/main.py --theme "Space Curiosities (a single curiosity)" \
  --language "en" \
  --voice_id "CstacWqMhJQlnfLPxRG4" \
  --max_duration 60 \
  --tts_service elevenlabs
```

### Example with OpenAI TTS

```bash
python src/main.py --theme "Technology Curiosities (a single curiosity)" \
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
- `--voice_id`: The voice ID to be used for narration (required for ElevenLabs).
- `--openai_tts_model`: The OpenAI TTS model to be used (default: `tts-1-hd`).
- `--openai_tts_voice`: The OpenAI TTS voice to be used (default: `alloy`).
- `--max_duration`: The maximum allowed duration for the audio (in seconds).

### Output:
The generated files will be saved in the `output/` folder, including:
- An audio file (`.mp3`) with the narration.
- A subtitle file (`.srt`) synchronized with the audio.
- A `process.log` file containing detailed logs of the process, including the prompts generated for each image interval.
- A final video (`_final.mp4`) assembled with animated transitions, maintaining a resolution of 1080x1920.

#### Subtitle Approach:
The subtitle generation process ensures better alignment and readability:
- **Punctuation Tokenization**: The full transcribed text is tokenized into words and punctuation, preserving the original order.
- **Word-Punctuation Alignment**: Each word is aligned with its corresponding token, ensuring correct punctuation placement.
- **Cue Segmentation**: Subtitles are divided into smaller segments (cues) based on character and word limits per line, maintaining synchronization with the audio timestamps.

---

## **Demonstration Videos**

### Demo 1
<video controls width="480">
  <source src="https://github.com/itallonardi/rapidclip-generator/blob/main/demos/en/space.mp4" type="video/mp4">
  Your browser does not support the video element.
</video>

### Demo 2
<video controls width="480">
  <source src="https://github.com/itallonardi/rapidclip-generator/blob/main/demos/en/technology.mp4" type="video/mp4">
  Your browser does not support the video element.
</video>

---

## **Project Status**

**RapidClip** is now in its first stable release. The core functionalities have been implemented and thoroughly tested, including:
- Generation of scripts, narration, subtitles, and images with diversified prompts.
- Final video assembly with animated transitions and a zoom-in effect on images, producing a final video at 1080x1920 resolution.
- Improved selection of images and application of visual effects.
- Detailed process logging with logs stored in each video's output folder.
- Support for configuring the SANA model version via an environment variable.

---

## **Next Steps**

1. Implement royalty-free background music integration.
2. Expand advanced video editing features for more sophisticated functionalities.

---

## **Contributions**

We welcome contributions! If you would like to collaborate on the project, please follow these steps:

1. Fork the repository.
2. Create a branch for your feature or bug fix:
   ```bash
   git checkout -b my-contribution
   ```
3. Make your changes and submit a pull request detailing your modifications.

Your help is greatly appreciated in making RapidClip even better!

---

## **License**

This project is licensed under the **MIT** license. This means you are free to use, modify, and distribute it, provided the original license is included in the code. Please refer to the [LICENSE](LICENSE) file for more details.