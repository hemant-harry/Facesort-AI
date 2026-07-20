from pathlib import Path
import shutil

from app.services.file_service import load_image
from app.services.face_service import get_face_embedding
from app.services.matcher import compare_faces

UPLOAD_FOLDER = Path("uploads")
OUTPUT_FOLDER = Path("output")

OUTPUT_FOLDER.mkdir(exist_ok=True)


def search_person(reference_embedding):

    # Clear previous results
    for file in OUTPUT_FOLDER.glob("*"):
        if file.is_file():
            file.unlink()

    matched_files = []

    for image_path in UPLOAD_FOLDER.glob("*"):

        if image_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
            continue

        image = load_image(image_path)

        if image is None:
            continue

        embedding = get_face_embedding(image)

        if embedding is None:
            continue

        is_match, similarity = compare_faces(reference_embedding, embedding)

        if is_match:

            destination = OUTPUT_FOLDER / image_path.name
            shutil.copy2(image_path, destination)

            matched_files.append({
                "file": image_path.name,
                "score": round(similarity, 3)
            })

    return matched_files