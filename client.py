import requests
from tts import main as make_audio
def post_voice(local_path):
    server_url = "http://localhost:8000/rapa"

    with open(local_path, "rb") as file:
        files = {"file": (local_path, file, "audio/wav")}
        response = requests.post(server_url, files=files).json()
    print(response)
    make_audio(response['answer_message'], './responsed_audio/responsd_audio_2.wav')
    return 0

post_voice('./recorded_audio/input_audio_2.wav')