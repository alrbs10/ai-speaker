import argparse
import os
import librosa
import soundfile as sf
from scipy.io import wavfile
from IPython.display import Audio
import wave
import pyaudio

from openai import OpenAI
from inference import Inferencer




def main(args):
    wav_path = args.path
    root_path = "C:/Users/지완/Documents/ASR" #server computer path
    sampling_rate = args.sr
    wav_file = os.path.join(root_path, '/' ,wav_path)
    print(wav_file)
    inferencer = Inferencer()
    output = inferencer.inference(wav_file)

    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str)
    parser.add_argument("--sr", type=int, default=16000)

    args = parser.parse_args()
    main(args)