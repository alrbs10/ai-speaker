from stt import transcribe_local_audio as get_text
from ask_gpt import create_response as make_text
def main(input_audio_file_path):
    question = get_text(input_audio_file_path)
    # question = 'what can i do for refreshing my mood?'
    # print("You've asked")
    # print(question)
    print("Additional Info: Women / 20")
    sex = '여자'
    age = '20'
    answer = make_text(sex=sex, age=age, request_message=question)
    print("Answer: ", end="")
    print(answer)
    return answer