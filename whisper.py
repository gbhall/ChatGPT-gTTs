import os
import sounddevice as sd
import soundfile as sf
from openai import OpenAI
client = OpenAI()

# Function to record audio from the default input device
def record_audio():
    duration = 5 # seconds
    samplerate = 44100
    print("Recording...")
    samples = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    print("Done recording.")
    return samples, samplerate

# Function to save the recorded audio to a file
def save_audio(samples, samplerate):
    filename = "audio.wav"
    sf.write(filename, samples, samplerate=samplerate)
    return filename

# Function to transcribe the audio using OpenAI API
def transcribe_audio(filename):
    print("Transcribing...")
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=file
        )
        print("Transcription:", transcription.text)
        return transcription

# Function that uses the above functions to record, save and transcribe audio
def record_and_transcribe_audio():
    samples, samplerate = record_audio()
    filename = save_audio(samples, samplerate)
    transcription = transcribe_audio(filename)
    os.remove(filename)
    return transcription

# Driver code
if __name__ == '__main__':
    transcription = record_and_transcribe_audio()
    print(transcription)
