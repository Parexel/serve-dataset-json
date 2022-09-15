from typing import Union
from fastapi import FastAPI
from JSONManager import JSONManager


app = FastAPI()


@app.get("/jsons")
def get_all_jsons():
    """
    Retrieve all available DatasetJSON files.
    """
    return JSONManager().available_jsons()


@app.post("/jsons")
def register_json_path(json_path: str):
    """
    Register JSON file.
    """
    return JSONManager().register_json(json_path)  # Returns the new file's ID number.


@app.get("/jsons/{json_id}/datasets")
def get_all_datasets(json_id: int):
    """
    Retrieve all available Datasets for a given DatasetJSON.
    """
    return {}


@app.get("/jsons/{json_id}/datasets/{dataset_name}/metadata")
def get_dataset_metadata(json_id: int, dataset_name: str):
    """
    Retrieve metadata for the specified dataset.
    """
    return {}


@app.get("/jsons/{json_id}/datasets/{dataset_name}/observations")
def get_dataset_observations(json_id:      int,
                             dataset_name: str,
                             page:         Union[int, None],
                             page_size:    Union[int, None],
                             query:        Union[str, None]):
    """
    Retrieve observations for the specified dataset.
    """
    return []
