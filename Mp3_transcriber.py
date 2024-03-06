import os
import argparse
import time
import openai

def transcribe_mp3_files(input_directory, output_directory, api_key, model="davinci"):
    """Transcribes multiple MP3 files using OpenAI's API.

    Args:
        input_directory: Path to the directory containing MP3 files.
        output_directory: Path to the directory to save transcriptions.
        api_key: Your OpenAI API key.
        model: Name of the model to use (e.g., 'davinci', 'curie', 'babbage').
    """

    print("Setting OpenAI API key...")
    openai.api_key = api_key
    print("API key set.\n")

    # Create the input and output directories if they don't exist
    os.makedirs(input_directory, exist_ok=True)
    os.makedirs(output_directory, exist_ok=True)

    print("Starting transcription process...")

    for filename in os.listdir(input_directory):
        if filename.endswith(".mp3"):
            file_path = os.path.join(input_directory, filename)
            print(f"Transcribing {file_path}...")

            try:
                with open(file_path, "rb") as file:
                    start_time = time.time()  # Measure transcription time
                    result = openai.Audio.create_transcription(
                        file=file,
                        model=model
                    )
                    end_time = time.time()

                # Print the transcription
                print(result.transcription)
                print(f"Transcription time: {end_time - start_time:.2f} seconds\n")

                # Save the transcription to a text file
                output_filename = os.path.splitext(filename)[0] + ".txt"
                output_path = os.path.join(output_directory, output_filename)
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(result.transcription)

            except Exception as e:
                print(f"Error transcribing {file_path}: {e}")

    print("Transcription process finished.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe MP3 files with OpenAI's API")
    parser.add_argument("input_directory", help="Path to the directory containing MP3 files")
    parser.add_argument("output_directory", help="Path to the directory to save transcriptions")
    parser.add_argument("api_key", help="Your OpenAI API key")
    parser.add_argument("--model", default="davinci", help="Name of the model to use")
    args = parser.parse_args()

    if not os.path.isdir(args.input_directory):
        print(f"Error: The input directory '{args.input_directory}' does not exist.")
    elif not os.path.isdir(args.output_directory):
        print(f"Error: The output directory '{args.output_directory}' does not exist.")
    else:
        transcribe_mp3_files(args.input_directory, args.output_directory, args.api_key, args.model)
