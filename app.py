from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os
import numpy as np
from src.cnnClassifier.pipeline.prediction_pipeline import PredictionPipeline

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Trang chủ"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/train")
async def train():
    """Chạy training pipeline"""
    os.system("python main.py")
    return "Training Successful!"


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    fixed_acidity: float = Form(...),
    volatile_acidity: float = Form(...),
    citric_acid: float = Form(...),
    residual_sugar: float = Form(...),
    chlorides: float = Form(...),
    free_sulfur_dioxide: float = Form(...),
    total_sulfur_dioxide: float = Form(...),
    density: float = Form(...),
    pH: float = Form(...),
    sulphates: float = Form(...),
    alcohol: float = Form(...)
):
    """Dự đoán chất lượng rượu vang"""
    try:
        # Tạo input array từ form data
        features = np.array([[
            fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
            chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
            density, pH, sulphates, alcohol
        ]])
        
        # Dự đoán
        result = PredictionPipeline().predict(features)
        
        return templates.TemplateResponse(
            "results.html", 
            {"request": request, "prediction": str(result)}
        )
    except Exception as e:
        print(f"Error: {e}")
        return "Something went wrong!"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)