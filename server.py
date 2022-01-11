import uvicorn
import threading
import asyncio
import os
from typing import Optional
from fastapi import FastAPI, Response, status
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


# classes
class InferenceInput(BaseModel):
    """
    Input values for model inference
    """

    sepal_length: float = Field(..., example=3.1, gt=0, title="sepal length (cm)")
    sepal_width: float = Field(..., example=3.5, gt=0, title="sepal width (cm)")
    petal_length: float = Field(..., example=3.4, gt=0, title="petal length (cm)")
    petal_width: float = Field(..., example=3.0, gt=0, title="petal width (cm)")


class ErrorResponse(BaseModel):
    """
    Error response for the API
    """

    error: bool = Field(..., example=True, title="Whether there is error")
    message: str = Field(..., example="", title="Error message")
    traceback: str = Field(None, example="", title="Detailed traceback of the error")


# routes
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/")
def read_root():
    return {"Hello": "Folks"}


@app.post("/imagebuild")
@app.post("/imagebuild/<imagetype>/<finalimagename>/<tag>")
def imagebuild(imagetype, finalimagename, tag, response: Response):
    print(f"imagetype:{imagetype}")
    if imagetype == None or finalimagename == None or tag == None:
        response = {"result": "Mandatory parameters may be missing"}
        response.status_code = 400
        return response
    else:
        if imagetype in ["prebuild", "scratch"]:
            # print(f"Inside flask function: {threading.current_thread().name}")
            asyncio.set_event_loop(asyncio.new_event_loop())
            loop = asyncio.get_event_loop()
            result = loop.run_until_complete(
                builddockerimage(imagetype, finalimagename, tag)
            )
            response = {"result": result}
            response.status_code = 201
            return response
        else:
            response = {
                "result": "Unprocessable Entity",
                "AllowedImagetypes": ["prebuild", "scratch"],
            }
            response.status_code = 422
            return response


# functions
# docker build -t simpleiris:latest --build-arg MYAPP_IMAGE=python:3.7-slim-buster --build-arg PORT=8000 .
async def builddockerimage(imagetype, finalimagename, tag):
    try:
        dockerfiletemplate = f"./docker/dockerfile{imagetype}"
        publishedimagename = f"{finalimagename}_{imagetype}:{tag}"
        proc = await asyncio.create_subprocess_exec(
            "docker",
            "build",
            "-f",
            dockerfiletemplate,
            "-t",
            publishedimagename,
            ".",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        result = await proc.wait()
        return result, publishedimagename
    except:
        return "failure"


if __name__ == "__main__":
    # server api
    uvicorn.run("server:app", host="0.0.0.0", port=8080, reload=True, debug=True)
