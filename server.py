from fastapi import FastAPI, File, UploadFile, HTTPException
from virtual_model import main
api = FastAPI()

@api.post("/rapa")
async def create_upload_file(file: UploadFile = File(...)):
    if file.content_type != "audio/wav":
        raise HTTPException(status_code=400, detail="Unsupported file format. Only WAV files are allowed.")
    contents = await file.read()
    save_audio_path = f'./server_uploaded/trial_2.wav'
    with open(save_audio_path, "wb") as f:
            f.write(contents)
    ans_text = main(save_audio_path)
    return {"answer_message": ans_text}
