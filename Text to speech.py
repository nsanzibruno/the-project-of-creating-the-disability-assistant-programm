# import three libraries
import asyncio
import edge_tts
from playsound import playsound
# use a default voice from playsound
VOICE = 'en-AU-NatashaNeural'
#name the file in which to play the sound
OUTPUT_FILE = "test.mp3"
# make functions for the generating the Audio
async def amain(text: str) -> None:
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(OUTPUT_FILE)

def play_audio(file_path):
    playsound(file_path)
# making it possible to enter more than one text at time
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