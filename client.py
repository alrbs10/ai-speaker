import requests
from tts import main as make_audio
from time import sleep
# def post_voice(local_path):
# server_url = "http://localhost:8000/rapa"

# with open(local_path, "rb") as file:
#     files = {"file": (local_path, file, "audio/wav")}
#     response = requests.post(server_url, files=files).json()
#     print(response)
#     make_audio(text = response['answer_message'], save_path = './responsed_audio/live_demo_answer.wav')
#     return 0

# post_voice('./recorded_audio/live_demo.wav')
res = requests.get('http://192.168.67.137:22222/check')
print(res)