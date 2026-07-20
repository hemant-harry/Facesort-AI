from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from pathlib import Path
import shutil

from app.services.file_service import load_image
from app.services.face_service import get_face_embedding
from app.services.search_service import search_person
from app.services.zip_service import create_zip

router = APIRouter()

UPLOAD_FOLDER = Path("uploads")
REFERENCE_FOLDER = Path("reference")

UPLOAD_FOLDER.mkdir(exist_ok=True)
REFERENCE_FOLDER.mkdir(exist_ok=True)

zip_file = Path("matched_images.zip")

if zip_file.exists():
    zip_file.unlink()


@router.post("/upload")
async def upload(
    folder: list[UploadFile] = File(...),
    reference: UploadFile = File(...)
):

    # Clear old uploaded images
    for file in UPLOAD_FOLDER.glob("*"):
        if file.is_file():
            file.unlink()

    # Clear old reference image
    for file in REFERENCE_FOLDER.glob("*"):
        if file.is_file():
            file.unlink()

    # Save uploaded folder images
    for image in folder:

        filename = Path(image.filename).name
        destination = UPLOAD_FOLDER / filename

        with open(destination, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

    # Save reference image
    reference_filename = Path(reference.filename).name
    reference_path = REFERENCE_FOLDER / reference_filename

    with open(reference_path, "wb") as buffer:
        shutil.copyfileobj(reference.file, buffer)

    # Load reference image
    reference_image = load_image(reference_path)

    if reference_image is None:
        return {
            "success": False,
            "message": "Failed to load reference image."
        }

    # Generate face embedding
    embedding = get_face_embedding(reference_image)

    if embedding is None:
        return {
            "success": False,
            "message": "No face detected in reference image."
        }

    # Search matching images
    matches = search_person(embedding)

    return {
        "success": True,
        "matched_images": len(matches),
        "files": matches
    }


@router.get("/download")
async def download():

    zip_path = create_zip()

    return FileResponse(
        path=zip_path,
        filename="matched_images.zip",
        media_type="application/zip"
    )