import platform
import subprocess
import whisper
import pyaudio
import wave
import numpy as np

def record_audio_rpi(output_file="audio.wav", duration=5):
    """
    Record audio on Raspberry Pi using arecord.
    """
    print("Recording on Raspberry Pi... Speak now.")
    command = f"arecord -D plughw:1,0 -f cd -t wav -d {duration} -r 16000 {output_file}"
    subprocess.run(command, shell=True, check=True)
    print(f"Audio saved to {output_file}")


def record_audio_in_memory(duration=5, rate=16000, chunk=1024):
    """
    Record audio in memory using PyAudio.
    """
    print("Recording... Speak now.")
    FORMAT = pyaudio.paInt16  # 16-bit audio format
    CHANNELS = 1  # Mono audio
    audio_interface = pyaudio.PyAudio()

    # Open a recording stream
    stream = audio_interface.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=rate,
                                  input=True,
                                  frames_per_buffer=chunk)
    frames = []
    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio_interface.terminate()

    # Combine frames into a single numpy array
    audio_data = np.frombuffer(b"".join(frames), dtype=np.int16)
    print("Recording complete.")
    audio_data = audio_data.astype(np.float32) / 32768.0
    return audio_data

def transcribe_audio_in_memory(model, audio_data, rate=16000):
    """
    Transcribe audio data from memory using Whisper.
    """
    print("Transcribing...")
    result = model.transcribe(audio_data, fp16=False, language="en")
    return result["text"]

def detect_platform():
    """
    Detect the current platform (Raspberry Pi or other).
    """
    if "arm" in platform.uname().machine:
        return "rpi"
    return "computer"


def speech_to_text(model, audio_file="audio.wav"):
    """
    Transcribe audio to text using Whisper.
    """
    print("Transcribing audio...")
    result = model.transcribe(audio_file)
    return result["text"]


if __name__ == "__main__":
    # Detect the platform
    platform_type = detect_platform()
    print(f"Detected platform: {platform_type}")

    # Load Whisper model
    print("Loading Whisper model...")
    model = whisper.load_model("tiny")  # Use "tiny" for better performance on limited hardware

    # Record and transcribe audio
    output_file = "audio.wav"
    if platform_type == "rpi":
        record_audio_rpi(output_file)
        transcription = speech_to_text(model, output_file)
    else:
        duration = 5
        audio_data = record_audio_in_memory(duration=duration)
        transcription = transcribe_audio_in_memory(model, audio_data)

    # Transcribe the audio
    print(transcription[1:])
    with open("transcription.txt", "w", encoding="utf-8") as file:
        file.write(transcription[1:])
