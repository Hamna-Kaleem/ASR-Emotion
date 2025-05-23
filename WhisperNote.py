
# Step 1: Install required libraries
!pip install -q openai-whisper torchaudio transformers librosa gradio

import whisper
import torch
import gradio as gr
from transformers import pipeline


# Load Whisper model (base or tiny for speed)
whisper_model = whisper.load_model("base")

# Load emotion classification pipeline
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)



def process_audio(audio):
    # Transcribe audio
    result = whisper_model.transcribe(audio)
    text = result["text"]

    # Get emotion prediction
    emotion = emotion_pipeline(text)[0]

    return f"Transcript:\n{text}\n\nEmotion: {emotion['label']} (Confidence: {emotion['score']:.2f})"



interface = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(sources="upload", type="filepath"),
    outputs="text",
    title="🎙️ WhisperNote: Audio to Text + Emotion Detection",
    description="Upload a voice note. We'll transcribe and analyze your emotion!"
)

interface.launch()
