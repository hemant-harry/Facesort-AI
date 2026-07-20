from pathlib import Path

from app.services.file_service import load_image
from app.services.face_service import get_face_embedding

reference_folder = Path("reference")

images = list(reference_folder.glob("*"))

if not images:
    print("No reference image found.")
    exit()

image = load_image(images[0])

if image is None:
    print("Failed to load image")
    exit()

embedding = get_face_embedding(image)

if embedding is None:
    print("No Face Found")
else:
    print("✅ Face Detected")
    print("Embedding Shape:", embedding.shape)