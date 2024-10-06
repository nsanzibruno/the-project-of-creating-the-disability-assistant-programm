# import three libraries
# I wanted to use elevenlabs but it didn't get easier for me
#I used these three that can be installed by using pip install

import asyncio
import edge_tts
from playsound import playsound

# use a default voice from playsound, there are
#different voice, search for the list and you can pick any

VOICE = 'en-AU-NatashaNeural'

#name the file in which to play the sound, 
#if you want you can also use vlc as the audio output

OUTPUT_FILE = "test.mp3"

# make functions for the generating the Audio

async def amain(text: str) -> None:
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(OUTPUT_FILE)

def play_audio(file_path):
    playsound(file_path)
    
# making it possible to enter more than one text at time
#and the options to end the repeating loop

if __name__ == "__main__":
    # make the while loop for the code to repeat as more times as possible
    while True:
        TEXT = input("Enter text (or type 'stop' to end): ")
        # the break option for the code
        if TEXT.lower() == 'stop':
            break
        asyncio.run(amain(TEXT))
        play_audio(OUTPUT_FILE)
        
# it was not an advanced as possible
# guys, you can add you own as I put the comments to direct
#you in the process
# Thanks, I can add other features that seem to be important
