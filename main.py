import sys
from whisper import record_and_transcribe_audio
from chatgpt import generate_chatgpt_response
from cute_voice import create_cute_voice

# Driver code
if __name__ == '__main__':
    transcription = record_and_transcribe_audio()["text"]
    response = generate_chatgpt_response(transcription)
    if response['choices'] and response['choices'][0]['message']:
        message = response['choices'][0]['message']['content']
        print(message)
        create_cute_voice(message)
    else:
        print('Failed to generate a response from ChatGPT API.')
        create_cute_voice("I'm having trouble connecting to the ChatGPT API.")
