from docx import Document
import nemo.collections.asr as nemo_asr
from pydub import AudioSegment
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
audio_file_path = os.getenv('AUDIO_FILE_PATH')
output_directory = os.getenv('OUTPUT_DIRECTORY')
docx_file_name = os.getenv('DOCX_FILE_NAME')

def split_audio(file_path, chunk_length_ms=50000):
    """Split the given audio file into chunks of the specified length in milliseconds."""
    audio = AudioSegment.from_file(file_path)
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunk.export(f"{output_directory}/chunk_{i//chunk_length_ms}.wav", format="wav")
        chunks.append(chunk)
    print(f"Total chunks created: {len(chunks)}")
    return [f"{output_directory}/chunk_{i//chunk_length_ms}.wav" for i in range(0, len(audio), chunk_length_ms)]

def transcribe_audio(files):
    """Transcribe given list of audio files and save to text files."""
    asr_model = nemo_asr.models.ASRModel.from_pretrained(model_name="stt_en_conformer_ctc_large")
    transcriptions = asr_model.transcribe(paths2audio_files=files)
    for i, transcription in enumerate(transcriptions):
        text_file_path = f"{output_directory}/chunk_{i}_transcription.txt"
        with open(text_file_path, 'w') as file:
            file.write(transcription)
        print(f"Chunk {i} transcription saved to {text_file_path}")

def create_docx_from_text_files(directory, output_file):
    """Create a DOCX file from text files in a directory."""
    doc = Document()
    for i in range(80):
        text_file_path = f"{directory}/chunk_{i}_transcription.txt"
        try:
            with open(text_file_path, 'r') as file:
                content = file.read()
                doc.add_paragraph(content)
                if i < 79:
                    doc.add_page_break()
        except FileNotFoundError:
            print(f"File not found: {text_file_path}")
        except Exception as e:
            print(f"Failed to read {text_file_path}: {e}")
    doc.save(output_file)
    print(f"Document saved as {output_file}")

if __name__ == "__main__":
    audio_chunks = split_audio(audio_file_path)
    transcribe_audio(audio_chunks)
    create_docx_from_text_files(output_directory, f"{output_directory}/{docx_file_name}")
