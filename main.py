import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.presentation.controllers.pregunta_controller import pregunta_controller
from src.presentation.controllers.opciones_controller import opciones_controller
from src.presentation.controllers.encuesta_controller import encuesta_controller
from src.presentation.controllers.respuesta_controller import respuesta_controller

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pregunta_controller)
app.include_router(opciones_controller)
app.include_router(encuesta_controller)
app.include_router(respuesta_controller)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
    
