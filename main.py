from fastapi import FastAPI

app = FastAPI(
    title="MTSys - Codificação de Relatórios",
    version="1.0"
)


@app.get("/")
def inicio():
    return {
        "sistema": "MTSys Codificação",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "servico": "MTSys Codificação"
    }
