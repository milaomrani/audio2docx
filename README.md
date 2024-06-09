# Audio2Docx

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
