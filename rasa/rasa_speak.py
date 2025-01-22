import sys
import requests
from TTS.piper_speak import text_to_speech

def get_rasa_response(message):
    url = "http://localhost:5005/webhooks/rest/webhook"
    payload = {"message": message}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()[0]["text"]
    else:
        print("Error: Unable to get response from Rasa.")
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python piper_speak.py 'Your text here'")
        sys.exit(1)

    user_input = sys.argv[1]
    
    rasa_response = get_rasa_response(user_input)
    
    if rasa_response:
        text_to_speech(rasa_response)
