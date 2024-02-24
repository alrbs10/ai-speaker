from fastapi import FastAPI, File, UploadFile, HTTPException
from virtual_model import main as make_ans_text
api = FastAPI()
import os
from model.inference_age import Inferencer_age
from model.inference_sex import Inferencer_sex
root_path = "/Users/shimhamin/Documents/GitHub/ai-speaker/" 
inferencer_age_model = Inferencer_age()
inferencer_sex_model = Inferencer_sex()
import time

@api.post("/rapa")
async def create_upload_file(file: UploadFile = File(...)):
    start_time_1 = time.time()
    if file.content_type != "audio/wav":
        raise HTTPException(status_code=400, detail="Unsupported file format. Only WAV files are allowed.")
    contents = await file.read()
    save_audio_path = os.path.join(root_path,'server_uploaded',file.filename)
    with open(save_audio_path, "wb") as f:
        f.write(contents)
    print(f"file come, saved at {save_audio_path}")
    end_time_1 = time.time()
    print(f"for file recieving and saving, took {end_time_1 - start_time_1}sec")
    
    start_time_2 = time.time()
    ans_text = make_ans_text(inferencer_age_model, inferencer_sex_model, save_audio_path)
    end_time_2 = time.time()
    print(f"for making answer, took {end_time_2 - start_time_2}sec")
    
    try:
        os.remove(save_audio_path)
        print(f"Removed {save_audio_path}")
    except FileNotFoundError:
        print(f"File {save_audio_path} is not founded")
    except Exception as e:
        print(f"Sth gone wrong: {e}")
    print(f"Total elasped time: {time.time()-start_time_1}")
    return {"answer_message": ans_text}

@api.get("/check")
async def hi():
    print("hi")
    return {"message":"hi"}