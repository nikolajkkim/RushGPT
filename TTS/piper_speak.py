import subprocess
import sys
import os

def text_to_speech(text):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    piper_path = os.path.join(script_dir, 'piper', 'piper')

    if not os.path.isfile(piper_path):
        print(f"Error: The piper executable was not found at {piper_path}")
        return
    
    command = [piper_path, '--model', 'en_US-amy-medium.onnx', '--output-raw' ]
    
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    
    process.stdin.write(text.encode('utf-8')) 
    process.stdin.close()
    
    aplay = subprocess.Popen(['aplay', '-r', '22050', '-f', 'S16_LE', '-t', 'raw'], stdin=process.stdout)
    aplay.wait()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python piper_speak.py 'Your text here'")
        sys.exit(1)

    text_to_speech(sys.argv[1])
