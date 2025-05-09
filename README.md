# 🎙️ WhisperNote : Vibe-Detecting Voice App

> I was just messing around and thought — hey, what if I could hear what I *feel*? So, I made this little app. 💡

**WhisperNote** is a playful mini app built with Python, OpenAI Whisper, and GradIO. Upload your voice note — it’ll transcribe your speech and tell you the *vibe* (emotion) you’re giving off.

## 💾 Install Requirements

Just run this in Colab:

```bash
!pip install -q openai-whisper torchaudio transformers librosa gradio
```

## 🚀 How It Works

1. Upload an audio file
2. It’s transcribed using OpenAI Whisper
3. That text is sent to an emotion classifier from Hugging Face
4. You get the transcript and the emotion label — boom!

## 🔥 Run the App

```python
interface.launch()
```

Or launch directly in Google Colab for that no-setup magic 🪄

## 📦 Code Breakdown

* `whisper_model = whisper.load_model("base")`
* `emotion_pipeline = pipeline(...)`
* The `process_audio()` function does all the magic
* Powered by `gr.Interface()` for the cool UI

## ✨ Sample Output

```
Transcript:
I’m really excited to work on this project!

Emotion: joy (Confidence: 0.98)
```

## 😎 Why I Made This

Honestly? I just wanted to build something chill and creative with Whisper + Gradio. No servers, no stress, just good vibes and Python.

## 💡 Future Fun Ideas

* Add emojis for emotions 
* Multilingual support 🌍
* Live mic input 🎤

## 🧑‍💻 Built With Love

Drop a star ⭐ if you vibed with it!
