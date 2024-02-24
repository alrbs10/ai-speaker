from utils.stt import transcribe_local_audio as get_text
from utils.ask_gpt import create_response as make_text
from model.main import main as whisper_inf
import warnings
import time

warnings.filterwarnings("ignore", category=UserWarning, module="transformers")
def main(age_model, sex_model, input_audio_file_path):
    s_1 = time.time()
    question = get_text(input_audio_file_path)
    e_1 = time.time()
    print(f"STT took {e_1-s_1}sec")
    s_2 = time.time()
    # output_age, output_sex = whisper_inf(age_model, sex_model, input_audio_file_path)
    output_age = age_model.inference(input_audio_file_path)
    output_sex = sex_model.inference(input_audio_file_path)
    e_2 = time.time()
    print(f"whisper model took {e_2-s_2}sec")
    print(output_age, output_sex)
    age = '어른' if(output_age) else '어린이'
    sex = '남자' if (output_sex) else '여자'
    print(f"Additional Info: {sex} / {age}")
    
    s_3 = time.time()
    answer = make_text(sex=sex, age=age, request_message=question)
    e_3 = time.time()
    print(f"GPT answer making took {e_3-s_3}sec")
    print("Answer: ", end="")
    print(answer)
    return answer