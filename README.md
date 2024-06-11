# 🔈 Audio2Docx

Audio2Docx is a Python utility that converts audio files into Microsoft Word documents (.docx) by performing speech-to-text transcription using NVIDIA's NeMo toolkit.

## Features

- **Audio Splitting**: Splits long audio files into manageable chunks.
- **Speech Recognition**: Transcribes audio chunks using a pre-trained Conformer model from NVIDIA NeMo.
- **Document Creation**: Compiles transcriptions into a well-formatted DOCX file.

## Installation

Before running this script, ensure you have Python installed along with the following dependencies:
- Pydub
- python-docx
- NVIDIA NeMo
- python-dotenv

You can install the necessary Python packages using:
```bash
pip install pydub python-docx nemo_toolkit[all] python-dotenv
```

## Setup
- Environment Variables: Set up your environment variables in a .env file at the root of your project directory. You will need:
  - AUDIO_FILE_PATH: Path to the source audio file.
  - OUTPUT_DIRECTORY: Directory to save the output chunks and final DOCX.
  - DOCX_FILE_NAME: Name of the output DOCX file.

- Audio Format: Ensure your audio file is in a format supported by Pydub.

## Usage
Run the script with:
```bash
python main.py
```
This will:

  - Split the provided audio file into chunks.
  - Transcribe each chunk using NVIDIA's NeMo ASR.
  - Compile all transcriptions into a single DOCX file.

