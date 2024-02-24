import argparse
import os
import librosa
import soundfile as sf
from scipy.io import wavfile
from IPython.display import Audio
import wave

from openai import OpenAI
# from model.inference_age import Inferencer_age
# from model.inference_sex import Inferencer_sex
from model.only_execute import inference
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="transformers")
# inferencer_age = Inferencer_age()
# inferencer_sex = Inferencer_sex()

def main(age_mode, sex_model, wav_path):
    # wav_path = args.path
    root_path = "/Users/shimhamin/Documents/GitHub/ai-speaker/" 
    wav_file = os.path.join(root_path, wav_path)
    print("Received file:",wav_file)
    # output_age = inferencer_age.inference(wav_file)
    # output_sex = inferencer_sex.inference(wav_file)
    output_age = inference(age_mode, wav_file)
    output_sex = inference(sex_model, wav_file)
    return output_age, output_sex


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--path", type=str)
#     parser.add_argument("--sr", type=int, default=16000)

#     args = parser.parse_args()
#     main(args)