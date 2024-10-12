import asyncio
import edge_tts
from playsound import playsound
from transformers import pipeline
from langdetect import detect
import logging
import argparse
from tensorflow import keras

# Configuration settings
VOICE = 'en-AU-NatashaNeural'
OUTPUT_FILE = "test.mp3"

# Initialize the sentiment analysis pipeline
sentiment_analysis = pipeline("sentiment-analysis")

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function for generating the audio
async def amain(text: str) -> None:
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(OUTPUT_FILE)

def play_audio(file_path):
    playsound(file_path)

# Main function to process text and play audio
def process_text(text: str):
    try:
        # Detect language
        language = detect(text)
        logging.info(f"Detected language: {language}")

        # Analyze sentiment
        result = sentiment_analysis(text)[0]
        sentiment = result['label']
        score = result['score']
        
        # Log sentiment analysis result
        logging.info(f"Sentiment: {sentiment}, Score: {score:.2f}")
        
        # Generate and play audio
        asyncio.run(amain(text))
        play_audio(OUTPUT_FILE)
    except Exception as e:
        logging.error(f"Error processing text: {e}")

# Making it possible to enter more than one text at a time
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Text to Speech with Sentiment Analysis')
    parser.add_argument('--text', type=str, help='Text to convert to speech')
    args = parser.parse_args()

    if args.text:
        process_text(args.text)
    else:
        while True:
            TEXT = input("Enter text (or type 'stop' to end): ")
            if TEXT.lower() == 'stop':
                break
            process_text(TEXT)
