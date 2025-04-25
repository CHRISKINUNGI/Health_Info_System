from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.programs import api as programs_api
from app.clients import api as clients_api

def create_app():
    app = FastAPI(
        title="Basic Health Information System API",
        description="API for managing health programs.",
        version="0.2.0",
        openapi_url="/api/v1/openapi.json",
        docs_url="/api/v1/docs",
        redoc_url="/api/v1/redoc",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Adjust in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(programs_api.router, prefix="/api/v1", tags=["Programs"])
    app.include_router(clients_api.router, prefix="/api/v1", tags=["Clients"])

    return app

app = create_app()  # No need to overwrite the app instance

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
