import warnings
from sptt import *


def main_loop():
    # Ignore "FutureWarning"
    warnings.simplefilter("ignore", category=FutureWarning)

    print("Setup: ")
    # Get platform type (RasPi or Computer) and initialize Porcupine based on it
    platform_type = detect_platform()
    porcupine = init_porcupine(platform_type)

    print(f"Platform detected: {platform_type}")
    print(f"Porcupine model initialized.")

    # Initialize Whisper model
    whisper_model = init_whisper()

    print("Whisper loaded\n")
    # Set up audio input
    mic = pyaudio.PyAudio()
    mic_name = mic.get_default_input_device_info()["name"]
    print(f"Default audio device: {mic_name}")

    while True:
        # Wait for wake word. If 0, wake word was detected. If -1, KeyBoardInterrupt, so exit
        success = wait_for_wake(mic, porcupine)
        if not success:
            mic.terminate()
            exit()

        # Wake word detected, record question and transcribe
        transcribed_question = whisper_speech_to_text(whisper_model, mic, 5)


if __name__ == "__main__":
    try:
        main_loop()
    except Exception as e:
        print(f"[ERROR]: {e}")
