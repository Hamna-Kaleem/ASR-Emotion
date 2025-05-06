

# 📓 WhisperNote: Flask App for Audio Transcription and Emotion Detection

**WhisperNote** is a simple Flask-based web app built to run inside Google Colab. It lets you upload an audio file, transcribes the speech using OpenAI's Whisper model, and detects the emotion in the text using a Hugging Face emotion classifier.

---

## 🚀 Features

* Upload audio files (WAV, MP3, etc.) via a web form
* Transcribe audio to text using OpenAI Whisper
* Analyze text emotion using Hugging Face Transformers
* Fully operational inside Google Colab using `flask-ngrok`

---

## 🔧 Requirements

Run the following command in Colab to install dependencies:

```python
!pip install flask ngrok flask-ngrok openai-whisper transformers torchaudio
```

---

## 🧠 Models Used

* **Speech-to-Text**: [OpenAI Whisper (base)](https://github.com/openai/whisper)
* **Emotion Detection**: [j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base)

---

## 🛠 How It Works

1. Upload an audio file via the Flask form.
2. Flask saves the file and uses Whisper to transcribe it.
3. The resulting text is passed to an emotion classification pipeline.
4. JSON output is returned with the transcription, emotion, and confidence score.

---

## ▶️ How to Run in Google Colab

1. Upload the notebook to your Google Drive.
2. Open in Google Colab.
3. Run all cells.
4. Ngrok will give you a public link where the app will be live.

---


## 🧪 Sample Output

```json
{
  "transcript": "Today I feel grateful and full of energy.",
  "emotion": "joy",
  "confidence": 0.98
}
```

---

## 💡 Future Ideas

* Add multilingual emotion detection
* Visualize waveform and spectrogram
* Integrate pitch/MFCC analysis

