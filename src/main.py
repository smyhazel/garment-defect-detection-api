from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Garment Defect Detection API is running"}
