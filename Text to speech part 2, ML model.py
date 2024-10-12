
#importing the necessary libraries
import asyncio
import edge_tts
from playsound import playsound
from transformers import pipeline
from langdetect import detect
import logging
import argparse
from tensorflow import keras

# the voive setting and the output form, remember the voive 
#I used is optional
VOICE = 'en-AU-NatashaNeural'
OUTPUT_FILE = "test.mp3"

# then, here I initialized the sentiment analysis pipeline, using pipeline
sentiment_analysis = pipeline("sentiment-analysis")

# Set up logging with basicConfig
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Now I made the function to generate the audio, the same as previos one
# But then the information have to be recorded before the output
# so as to learn the user input
async def amain(text: str) -> None:
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(OUTPUT_FILE)

def play_audio(file_path):
    playsound(file_path)

# the main main function for the Audio generation
def process_text(text: str):
    try:
        # I don't how to use only Kinyarwanda but guys, I can use this library
        # to detect the user langauge
        language = detect(text)
        logging.info(f"Detected language: {language}")

        # Then the analysation of the sentiment
        result = sentiment_analysis(text)[0]
        sentiment = result['label']
        score = result['score']
        
        # here are the results of the sentiment analysis
        logging.info(f"Sentiment: {sentiment}, Score: {score:.2f}")
        
        # GEnerating the Audio from the text, using asyncio
        asyncio.run(amain(text))
        play_audio(OUTPUT_FILE)
    except Exception as e:
        logging.error(f"Error processing text: {e}")

# Making it possible to enter more than one text at a time,
# however this is not really working well
# I need some help on this loop because the second
#input is coming with an error
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Text to Speech with Sentiment Analysis')
    parser.add_argument('--text', type=str, help='Text to convert to speech')
    args = parser.parse_args()

    if args.text:
        process_text(args.text)
    else:
        # providing away for the user to stop providing in put
        while True:
            TEXT = input("Enter text (or type 'stop' to end): ")
            if TEXT.lower() == 'stop':
                break
            process_text(TEXT)
  # guys, It is important to install all the libraries and  set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`. 
# otherwise the code won't run
