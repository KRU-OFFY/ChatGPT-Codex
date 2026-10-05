# Project JSON schema

Paths resolve relative to the JSON file. Required fields are `output` and `clips`.

```json
{
  "output": "out/school-safety-vtr.mp4",
  "width": 1920,
  "height": 1080,
  "fps": 30,
  "max_duration_seconds": 290,
  "video_bitrate": "8M",
  "audio_bitrate": "192k",
  "clips": [
    {
      "path": "media/opening.mp4",
      "start": 0,
      "duration": 8,
      "brightness": 0.02,
      "contrast": 1.04,
      "saturation": 1.03,
      "volume": 0.35,
      "fade_in": 0.35,
      "fade_out": 0.35
    }
  ],
  "logo": {
    "path": "assets/school-logo.png",
    "width": 150,
    "margin": 36,
    "position": "top-right"
  },
  "subtitles": "captions/final.srt",
  "voiceover": {
    "path": "audio/voiceover.wav",
    "volume": 1.0
  },
  "music": {
    "path": "audio/music.mp3",
    "volume": 0.16,
    "ducking": true
  }
}
```

Valid logo positions: `top-left`, `top-right`, `bottom-left`, `bottom-right`.

Ranges:

- brightness: -1.0 to 1.0
- contrast: 0.0 to 2.0
- saturation: 0.0 to 3.0
- volume: 0.0 to 4.0
- fade values: non-negative seconds and no longer than the clip

The renderer trims clips in listed order. It uses clip audio when present and inserts silence when absent. Voice-over and music start at zero and are trimmed to the final picture duration.

