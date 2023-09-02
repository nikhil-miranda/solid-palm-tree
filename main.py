from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse

from app.core.events import create_start_app_handler, create_stop_app_handler
from app.routers import router as router


def get_application() -> FastAPI:
    application = FastAPI(
        title="solid-palm-tree",
        debug=True,
        version="0.1.0"
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.include_router(router)

    return application


app = get_application()


@app.get("/")
def root():
    text_content = """
    
    
                                             |
                      |                      |
                      |                    -/_\-
                    -/_\-   ______________(/ . \)______________
       ____________(/ . \)_____________    \___/          <>
          <>        \___/         <>

              Iceman: "You can be my wingman any time."
              Maverick: "Bull----! You can be mine." 
     
    """

    return PlainTextResponse(content=text_content)


@app.get("/health")
def health():
    return {"message": "I am Alive !!"}
