from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from minio import Minio
from minio.error import S3Error
import os
from builtins import str
from uuid import UUID
from settings.config import settings
from PIL import Image
from io import BytesIO

minio_client = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ACCESS_KEY,
    secret_key=settings.MINIO_SECRET_KEY,
    secure=False
)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_FILE_SIZE = 10 * 1024 * 1024 

async def upload(file: UploadFile, user_id: UUID) -> str:
    try:
        if not allowed_file(file):
            return "File type is not allowed"

        # Read the file data into memory
        file_data = await file.read()
        size = (200, 200)  # New size: width = 200, height = 200
        resized_image_data = resize_image(file_data, size, user_id)

        # Generate file name
        image_extension = file.filename.split('.')[-1]
        image_name = f"{user_id}.{image_extension}"

        # Upload the resized image to Minio
        minio_client.put_object(
            settings.MINIO_BUCKET_NAME,
            image_name,
            resized_image_data,
            resized_image_data.getbuffer().nbytes
        )

        # Return success response
        return f"http://{settings.MINIO_ENDPOINT}/{settings.MINIO_BUCKET_NAME}/{image_name}"
    except S3Error as exc:
        print("error occurred.", exc)
        return None

def allowed_file(file: UploadFile):
    filename = file.filename
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def resize_image(file_data, size, user_id):
    with Image.open(BytesIO(file_data)) as img:
        resized_img = img.resize(size)
        output = BytesIO()
        resized_img.save(output, format=img.format)
        output.seek(0)
        return output
