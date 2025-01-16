import subprocess
import sys

def text_to_speech(text):
    command = ['./piper/piper', '--model', 'en_US-amy-medium.onnx', '--output-raw' ]
    
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
