from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="FarmIA - Predição de Área de Irrigação")

# Modelo treinado carregado com joblib
modelo_FarmIa = joblib.load('../ia/Modelo_FarmIa.pkl')


# Modelo do corpo da requisição
class RequestBody(BaseModel):
    horas_regacao: float


# Rota de predição
@app.post("/predict")
def predict(data: RequestBody):
    # Transformar entrada em formato de matriz (para o modelo)
    input_feature = np.array([[data.horas_regacao]])

    # Fazer a predição
    y_pred = modelo_FarmIa.predict(input_feature)

    # Converter resultado para tipo nativo Python
    resultado = float(y_pred[0])

    return {"area_prevista": resultado}


# Rota raiz
@app.get("/")
def raiz():
    return {"mensagem": "🌾 API de predição de área de irrigação funcionando!"}
