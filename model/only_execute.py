import torch

def inference(model, wav_file):
    sampling_rate = 16000 #assert
    wav_file = model.preprocess(wav_file) #file_name으로 전달하면 tensor로 return

    output = model.model.forward(wav_file)
    output = output[0]
    predict_label = torch.argmax(output, dim=1)

    return predict_label