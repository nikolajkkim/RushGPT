Uses OpenAI Whisper to transcribe audio.

**Installation** (Windows):

Run this command in the terminal to install required dependencies: 

*pip install pyaudio whisper torch torchvision torchaudio*

Run this command to test functionality:

*python whisper_main.py*

**Installation** (RasPi):

Run these commands in the terminal to install required dependencies:

*sudo apt update*

*sudo apt install ffmpeg*

*pip install git+https://github.com/openai/whisper.git*

*pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu*

Ensure that your audio capturing device is accurate:

*arecord -1*

Update the *-D plughw:1,0* in record_audio_rpi to match your microphone's device ID


