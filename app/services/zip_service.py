from pathlib import Path
import zipfile

OUTPUT_FOLDER = Path("output")
ZIP_FILE = Path("matched_images.zip")


def create_zip():

    if ZIP_FILE.exists():
        ZIP_FILE.unlink()

    with zipfile.ZipFile(ZIP_FILE, "w", zipfile.ZIP_DEFLATED) as zipf:

        for image in OUTPUT_FOLDER.glob("*"):

            if image.is_file():
                zipf.write(image, arcname=image.name)

    return ZIP_FILE