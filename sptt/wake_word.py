import os
from dotenv import load_dotenv
import pvporcupine
import struct
import pyaudio


def init_porcupine(platform_typ: str):
    # Load environment variables from .env file
    load_dotenv()
    access_key = os.getenv("PICOVOICE_API_KEY")

    if not access_key:
        raise ValueError("Missing API key. Make sure to set it in a .env file.")

    if platform_typ == "computer":
        porcupine = pvporcupine.create(access_key=access_key, keywords=["computer", "jarvis"])
        return porcupine

    porcupine = porcupine = pvporcupine.create(access_key=access_key, keyword_paths=["./Hey-Rush-Bot_en_raspberry-pi_v3_0_0.ppn"])
    return porcupine


def wait_for_wake(p, porcupine):
    stream = p.open(rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)
    print("Listening for the wake word...")
    try:
        while True:
            # Read a frame of audio
            pcm = stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            # Check for wake word detection
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Wake word detected!")
                return 1
    except KeyboardInterrupt:
        print("Exiting...")
        return 0
    finally:
        stream.stop_stream()
        stream.close()
