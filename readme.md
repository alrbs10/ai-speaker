# 라즈베리파이를 사용한 나만의 스피커 만들기
팀원 HW : 심하민, 성원희, 윤재선 
팀원 SW : 지완 , 은주 , 경현

#Server

- listen for request(especially post request for our project)
- when get post request at endpoint('rapa'), upload file content to /server_uploaded
- read file from that path, and process data(model part)
- finally, return text answer data

# Client(Raspberry pi board)

- request some tasks to server
- when .wav file is recorded by user(=human), it requests server to make appropriate response for that input audio, considering the user(=human)'s sex and age
- finally, gets answer text from server and make that answer to audio file using google TTS, and speak that to user(=human)

# Explanation for python files

- server.py: utilizes server, to activate it, open terminal and type
  `uvicorn server:api --reload`
- client.py: after making .wav file(=audio input), save it to recorded_audio, and execute this file (with appropriate path designated)
- stt.py: google cloud speech-to-text, must activate auth(=json file) to use
- tts.py: same as stt.py, by google, must be activated first
- ask_gpt.py: requires extra info(=sex, age) and message from audio input which is transcripted by stt code
- virtual_model.py: not final model, just for brief validation for the system


