from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Criar instância do FastAPI
app = FastAPI()

# Classe para receber os dados do corpo da requisição
class RequestBody(BaseModel):
    horas_estudo: float

# Carregar o modelo treinado
modelo_pontuacao = joblib.load('./modelo_regressao.pkl')

# Criar rota POST para predição
@app.post('/predict')
def predict(data: RequestBody):
    # Preparar dados
    input_feature = [[data.horas_estudo]]

    # Fazer predição
    y_pred = modelo_pontuacao.predict(input_feature)[0].astype(int)

    return {"pontuacao_prevista": y_pred.tolist()}

@app.get('/')
def raiz():
    return {"mensagem": "API de predição de pontuação funcionando!"}

