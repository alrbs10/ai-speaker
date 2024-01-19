from stt import transcribe_local_audio as get_text
from ask_gpt import create_response as make_text
def main(input_audio_file_path):
    question = get_text(input_audio_file_path)
    # question = 'what can i do for refreshing my mood?'
    sex = 'women'
    age = '40'
    answer = make_text(sex=sex, age=age, request_message=question)
    print(answer)
    return answer