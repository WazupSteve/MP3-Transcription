# MP3 Transcription with OpenAI's API

This Python script provides a convenient way to transcribe multiple MP3 files using OpenAI's API. It's particularly useful for automating the transcription process, saving time and effort.

## Features

- Transcribes multiple MP3 files in bulk.
- Utilizes OpenAI's powerful models for accurate transcriptions.
- Easy-to-use command-line interface (CLI) with argument parsing.
- Saves transcriptions as text files for easy reference.

## Prerequisites

Before using this script, ensure you have the following:

- Python 3.x installed on your system.
- An OpenAI API key. You can get one by signing up on the OpenAI website.
- MP3 files you want to transcribe stored in a directory.

## Installation

1. Clone or download this repository to your local machine.
2. Install the required Python dependencies using pip:

```bash
pip install openai
```

## Usage

1. Navigate to the directory where you've cloned/downloaded the script.
2. Run the script using the following command:

```bash
python transcribe_mp3.py [input_directory] [output_directory] [api_key] [--model MODEL]
```

Replace `[input_directory]`, `[output_directory]`, and `[api_key]` with your specific directories and API key. Additionally, you can specify the model to use (optional, default is 'davinci').

Example:

```bash
python transcribe_mp3.py input_files/ output_transcriptions/ YOUR_API_KEY --model curie
```

## Command-Line Arguments

- `input_directory`: Path to the directory containing MP3 files.
- `output_directory`: Path to the directory to save transcriptions.
- `api_key`: Your OpenAI API key.
- `--model`: (Optional) Name of the model to use (e.g., 'davinci', 'curie', 'babbage'). Default is 'davinci'.

## Example

Suppose you have a directory named `audio_files` containing MP3 files you want to transcribe. You want to save the transcriptions in a directory named `transcriptions_output`. Your OpenAI API key is `YOUR_API_KEY`. You want to use the 'curie' model for transcription. You would run the script as follows:

```bash
python transcribe_mp3.py audio_files/ transcriptions_output/ YOUR_API_KEY --model curie
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to OpenAI for providing the powerful models and API used in this script.
