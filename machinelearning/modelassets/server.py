import uvicorn
import threading
import asyncio
import os
from typing import Optional
from fastapi import FastAPI, Response, status
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException as StarletteHTTPException
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
import pickle


app = FastAPI()


# useful variables
global iris_loaded_model  # declare a global variable to avoid unnecessary reloads
iris_prediction_mapper = {0: "Iris-Setosa", 1: "Iris-Versicolour", 2: "Iris-Virginica"}


class Item(BaseModel):
    sepal_length_in_cm: float
    sepal_width_in_cm: float
    petal_length_in_cm: float
    petal_width_in_cm: float


def model_load():
    # load the classifier model
    try:
        iris_loaded_model = pickle.load(open("./iris_model.sav", "rb"))
        return iris_loaded_model
    except Exception as e:
        print(f"Model Load Error {str(e)}")


def prediction(loaded_model, array_of_features):
    if loaded_model:  # only if the model is there
        prediction_result = loaded_model.predict(array_of_features)
        try:
            species_type = iris_prediction_mapper.get(prediction_result[0])
            return species_type
        except KeyError:
            species_type = "Could Not Be Determined"
            return species_type


@app.post("/predictiris")
def predictiris(item: Item, response: Response):
    prediction_input = jsonable_encoder(item)
    # attempt model load
    loaded_model = model_load()
    print(prediction_input)
    output = prediction(
        loaded_model, [[float(item) for item in list(prediction_input.values())]]
    )  # as the form data conatins the values in string
    response = {"result": f"Species is {output}"}
    return response


@app.get("/")
@app.get("/healthcheck")
def healthcheck(response: Response):
    response = {"result": "Success", "response": "Healthcheck performed succesfully"}
    return response


if __name__ == "__main__":
    # server api
    uvicorn.run("server:app", host="0.0.0.0", port=8081, reload=True, debug=True)
