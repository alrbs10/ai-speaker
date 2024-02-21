from fastapi import FastAPI, File, UploadFile, HTTPException
from virtual_model import main
api = FastAPI()
import os


@api.post("/rapa")
async def create_upload_file(file: UploadFile = File(...)):
    if file.content_type != "audio/wav":
        raise HTTPException(status_code=400, detail="Unsupported file format. Only WAV files are allowed.")
    contents = await file.read()
    save_audio_path = f'./server_uploaded/{file.filename}.wav'
    with open(save_audio_path, "wb") as f:
            f.write(contents)
    print(f"file come, saved at {save_audio_path}")
    ans_text = main(save_audio_path)

    try:
        os.remove(save_audio_path)
        print(f"Removed {save_audio_path}")
    except FileNotFoundError:
        print(f"File {save_audio_path} is not founded")
    except Exception as e:
        print(f"Sth gone wrong: {e}")
    return {"answer_message": ans_text}

@api.get("/check")
async def hi():
    print("hi")
    return {"message":"hi"}