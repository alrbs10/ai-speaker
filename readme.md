# 라즈베리파이를 사용한 나만의 스피커 만들기
팀원 HW : 심하민, 성원희, 윤재선 <br/>
팀원 SW : 지완 , 은주 , 경현 <br/>
[Notion] 


# Server

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


# SW Team
<img width="1406" alt="image" src="https://github.com/alrbs10/ai-speaker/assets/102707496/0e54e9e0-aa17-41a6-a491-312e1418675b">
<br/>
- 초기 계획 : HW 팀으로 부터 받은 음성파일을 형태소 분석 , 구문 분석 , 의미 분석 , 담화 분석을 통해 그에 알맞는 언어를 생성한 후 다시 음성파일로 변환 후에 HW 팀으로 다시 넘긴다.
<br/>

## STT , TTS 에 사용한 OpenAI Whisper model
https://openai.com/research/whisper
<br/>
<img width="854" alt="image" src="https://github.com/alrbs10/ai-speaker/assets/102707496/e3e63b0b-c3b2-408a-94e1-b7db0b0583df">
<br/>
Whisper is an automatic speech recognition (ASR) system trained on 680,000 hours of multilingual and multitask supervised data collected from the web. We show that the use of such a large and diverse dataset leads to improved robustness to accents, background noise and technical language. Moreover, it enables transcription in multiple languages, as well as translation from those languages into English. We are open-sourcing models and inference code to serve as a foundation for building useful applications and for further research on robust speech processing.

<img width="590" alt="image" src="https://github.com/alrbs10/ai-speaker/assets/102707496/61a6bffe-91ee-4aa0-9be1-ed836e7c9585">

- whisper STT 를 사용하여 음성을 텍스트로 변환한다음 모델을 통하여 화자정보를 추출
- 이에 화자정보에 따른 rule-based의 프롬프트 튜닝을 거쳐 gpt api를 사용, input text에 맞는 텍스트를 생성
- 생성된 텍스트를 whisper TTS 를 사용하여 음성파일의 형태로 변환하는 작업을 거침

## 화자 분류에 사용된 모델 및 데이터셋
![image](https://github.com/alrbs10/ai-speaker/assets/102707496/bc75fd33-e2ac-47a3-8c38-475429266dda)


