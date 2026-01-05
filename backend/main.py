from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os, uuid, shutil

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITES_DIR = os.path.join(BASE_DIR, "sites")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

os.makedirs(SITES_DIR, exist_ok=True)

app.mount("/sites", StaticFiles(directory=SITES_DIR, html=True), name="sites")

@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    with open(os.path.join(FRONTEND_DIR, "index.html"), "r", encoding="utf-8") as f:
        return f.read()

@app.post("/upload")
async def upload_files(files: list[UploadFile] = File(...)):
    site_id = uuid.uuid4().hex[:10]
    site_path = os.path.join(SITES_DIR, site_id)
    os.makedirs(site_path, exist_ok=True)

    has_index = False

    for file in files:
        file_path = os.path.join(site_path, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        if file.filename.lower() == "index.html":
            has_index = True

    if not has_index:
        shutil.rmtree(site_path)
        return JSONResponse(
            status_code=400,
            content={"detail": "index.html is required"}
        )

    return {
        "url": f"http://127.0.0.1:8000/sites/{site_id}/"
    }
