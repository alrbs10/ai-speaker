import pyaudio
import wave
import RPi.GPIO as GPIO
import time
import requests
import pygame
from api import main
import time
import os
pygame.mixer.init()
def play_wav_file(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

switch1 = 6  # switch GPIO Num
record_flag = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch1, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Switch setting input

form_1 = pyaudio.paInt16
chans = 1
samp_rate = 44100
chunk = 4096
record_secs = 50
dev_index = 1
#recorded_file_name = 'testfile.wav'  # make file .wav

audio = pyaudio.PyAudio()
server_url = "http://192.168.20.212:22222/rapa"

while True:

    switch_state = GPIO.input(switch1)

    if switch_state == GPIO.LOW and not record_flag:
        print("Recording started")
        record_flag = True
        frames = []
        stream = audio.open(format=form_1, rate=samp_rate, channels=chans, input_device_index=dev_index, input=True,
                            frames_per_buffer=chunk)
        for _ in range(0, int((samp_rate / chunk) * record_secs)):
            if GPIO.input(switch1) == GPIO.HIGH:
                break
            data = stream.read(chunk)
            frames.append(data)
        print("Recording stopped")
        stream.stop_stream()
        stream.close()
        audio.terminate()
        recorded_file_name = f"{int(time.time())}.wav"
        wavefile = wave.open(recorded_file_name, 'wb')
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()
        with open(recorded_file_name, "rb") as file:
            files = {"file": (recorded_file_name, file, "audio/wav")}
            response = requests.post(server_url, files=files).json()
        print(response)
        response_file_name = f"{int(time.time())}.wav"
        main(response["answer_message"],response_file_name)
        play_wav_file(response_file_name)
        record_flag = False
        for saved_audio_path in [recorded_file_name, response_file_name]:
            try:
                os.remove(saved_audio_path)
                print(f"Removed {saved_audio_path}")
            except FileNotFoundError:
                print(f"File {saved_audio_path} is not founded")
            except Exception as e:
                print(f"Sth gone wrong: {e}")
    time.sleep(0.1)
