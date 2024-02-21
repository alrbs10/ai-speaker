from model.main import main as whisper_inf
import torch

output_age, output_sex = whisper_inf('./adult_women.wav')
# print(torch.Tensor.values()(output))
print(output_age, output_sex)
# if(output):
#     print("성인입니다")
# else:
#     print("어린 아이입니다.")