# Creates a cute voice for the given text using gTTS

import os
import sys
from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

# Function to create the cute voice
def create_cute_voice(text):
    tts = gTTS(text=text, lang='en', slow=False)
    filename = "cute_voice.mp3"
    tts.save(filename)

    # Increase the pitch of the sound
    sound = AudioSegment.from_file(filename, format="mp3")
    octaves = 0.5
    new_sample_rate = int(sound.frame_rate * (2 ** octaves))
    hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    hipitch_sound = hipitch_sound.set_frame_rate(44100)

    # Save the modified sound
    # high_pitch_filename = "cute_voice_high_pitch.mp3"
    # hipitch_sound.export(high_pitch_filename, format="mp3")

    # Play the modified sound directly from memory
    play(hipitch_sound)

    # Play the modified sound from the file
    # playsound(high_pitch_filename)

    # Remove the temporary files
    os.remove(filename)
    # os.remove(high_pitch_filename)

# Function to create the basic voice
def create_basic_voice(text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save('basic_voice.mp3')
    playsound('basic_voice.mp3')
    os.remove('basic_voice.mp3')    

# Driver code
if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) > 1:
        if sys.argv[1] == "-b" and len(sys.argv) > 2:
            text = sys.argv[2]
            create_basic_voice(text)
        else:
            text = sys.argv[1]
            create_cute_voice(text)
    else:
        text = input("Enter the text: ")
        create_cute_voice(text)
