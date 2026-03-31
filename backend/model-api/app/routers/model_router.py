from fastapi import APIRouter, Depends, HTTPException, Header
from app.internal.services.model_service import ModelService
from app.internal.services.security import verify_api_key

router = APIRouter()
model_service = ModelService()

@router.get("/")
async def hello():
    return {"message": "Hello from model-api"}

@router.get("/predict", dependencies=[Depends(verify_api_key)])
async def predict(features: list[float]):
    prediction = await model_service.predict(features)
    return {"prediction": prediction}