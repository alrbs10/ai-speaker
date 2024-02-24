# 라즈베리파이를 사용한 나만의 스피커 만들기
팀원 HW : 심하민, 성원희, 윤재선 <br/>
팀원 SW : 박지완 , 박은주 , 남경현 <br/>
<a href='https://elderly-podium-4c3.notion.site/4-ed35bd711dca48f5bd22625d26d42d87'>[Notion]</a>


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

## 화자 분류에 사용된 데이터셋
- 화자를 분류할 때 있어서 데이터셋이 중요했습니다.<br/>
- 먼저 어린아이와 성인의 화자 정보를 구분하기 위해 AI 허브의 어린이 음성 데이터셋을 사용하였습니다. 어린아이를 0 , 성인을 1로 라벨링 하였습니다.<br/>

<img width="854" alt="image" src="https://github.com/alrbs10/ai-speaker/assets/102707496/98efc24b-87f4-46b1-b84d-c4a2d4af6b73">

- 더 나아가 어린아이와 성인의 화자정보만 구분하는 것에더 더 나아가 남녀의 발화정보도 구분하였습니다. <br/>
- 성별을 구분하기 위해서 AI 허브의 한국어 음성을 사용하였습니다. 여자는 0 , 남자를 1로 라벨링 하였습니다.<br/>
<img width="854" alt="image" src="https://github.com/alrbs10/ai-speaker/assets/102707496/ab8fca85-219b-481e-b68f-9c6edee931b9">

## 화자 분류에 사용된 모델

## model
(openai/whisper-large) <br/>
### feature extractor (based on cnn)
![image](https://github.com/alrbs10/ai-speaker/assets/102707496/ed4ef235-daaa-4c72-aa8a-d11b2748467f)
### encoder (based on transformer) 
![image](https://github.com/alrbs10/ai-speaker/assets/102707496/ffa9f088-8a8c-4dc7-a61f-44e5f09eff1e)
### linear classifier layer
![image](https://github.com/alrbs10/ai-speaker/assets/102707496/19f25244-1ab3-47c7-a057-6ff9dec2a5cd)
<br/>

## model training
finetuing whisper <br/>
<br/>
<img width="854" alt="image" src="https://github.com/alrbs10/ai-speaker/assets/102707496/e3e63b0b-c3b2-408a-94e1-b7db0b0583df">
freeze model's feature extractor and encoder but train randomly initialized linear layer <br/>

# HW Team

# Explanation for python files
- audiolist.py: identify current audio input and output device number
- api.py: The given Python script utilizes Google Cloud's Text-to-Speech API to convert text into speech and save it as a file.
- finrecord.py: record audio and send it to server than get the appropriate audio file and output the audio file by speaker

