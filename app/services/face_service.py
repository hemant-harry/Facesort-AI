from insightface.app import FaceAnalysis

# Load AI model only once
app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0)

def get_face_embedding(image):
    """
    Returns the face embedding of the first detected face.
    """

    faces = app.get(image)

    if len(faces) == 0:
        return None

    return faces[0].embedding