import platform
import whisper
import pyaudio
import numpy as np


def detect_platform():
    """
    Detect the current platform (Raspberry Pi or other).
    """
    if "arm" in platform.uname().machine:
        return "rpi"
    return "computer"


def init_whisper():
    print("Loading Whisper model...")
    whisper_model = whisper.load_model("tiny")  # Use "tiny" for better performance on limited hardware
    return whisper_model


def record_audio_in_memory(audio_interface, duration=5, rate=16000, chunk=1024):
    """
    Record audio in memory using PyAudio.
    """
    print("Recording... Speak now.")
    FORMAT = pyaudio.paInt16  # 16-bit audio format
    CHANNELS = 1  # Mono audio

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

    # Combine frames into a single numpy array
    audio_data = np.frombuffer(b"".join(frames), dtype=np.int16)
    print("Recording complete.")
    audio_data = audio_data.astype(np.float32) / 32768.0
    return audio_data


def transcribe_audio_in_memory(whisper_model, audio_data, rate=16000):
    """
    Transcribe audio data from memory using Whisper.
    """
    print("Transcribing...")
    result = whisper_model.transcribe(audio_data, fp16=False, language="en")
    return result["text"]


def whisper_speech_to_text(whisper_model, audio, duration):
    # Record and transcribe audio
    audio_data = record_audio_in_memory(audio, duration=duration)
    transcription = transcribe_audio_in_memory(whisper_model, audio_data)

    # Transcribe the audio
    print(transcription[1:])
    return transcription


if __name__ == "__main__":
    model = init_whisper()
    mic = pyaudio.PyAudio()
    whisper_speech_to_text(model, mic, 5)
