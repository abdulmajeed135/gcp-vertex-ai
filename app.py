from fastapi import FastAPI, File, Form, UploadFile
from typing import List
from model import imagetotext
import json
import os

folder_name = "files"
app = FastAPI()

@app.get("/model/status")
def model_info():
    return {"status": "running"}

@app.post("/model/upload_image")
def model_upload_image(file: UploadFile):

    # create the uploads folder
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
       
    file_location = f"{folder_name}/{file.filename}"

    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    # parsing file to model function
    load_image = imagetotext(file_location)

    response = {
        "filename": file.filename,
        "Image Caption": load_image
    }
    
    os.remove(f"{folder_name}/{file.filename}")
    return response