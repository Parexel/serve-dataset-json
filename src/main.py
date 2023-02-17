import math
import src.queryparser as queryparser

from streamdatasetjson.dataset import Row
from typing import Optional
from fastapi import FastAPI, Body
from src.JSONManager import JSONManager


app = FastAPI()


@app.get("/jsons")
def get_all_jsons():
    """
    Retrieve all available DatasetJSON files.
    """
    return JSONManager().available_jsons()


@app.post("/jsons")
def open_json_path(path: str = Body(embed=True)):
    """
    Open JSON file.
    """
    return JSONManager().open(path)  # Returns the new file's ID number.


@app.delete("/jsons/{json_id}")
def close_json(json_id: int):
    """
    Close JSON file.
    """
    JSONManager().close(json_id)


@app.get("/jsons/{json_id}/datasets")
def get_all_datasets(json_id: int):
    """
    Retrieve all available Datasets for a given DatasetJSON.
    """
    return JSONManager().get(json_id).available_datasets


@app.get("/jsons/{json_id}/datasets/{dataset_name}/metadata")
def get_dataset_metadata(json_id: int, dataset_name: str):
    """
    Retrieve metadata for the specified dataset.
    """
    return JSONManager().dataset_metadata(json_id, dataset_name)


@app.get("/jsons/{json_id}/datasets/{dataset_name}/observations")
def get_dataset_observations(json_id:      int,
                             dataset_name: str,
                             page:         int = 1,
                             page_size:    int = 1000,
                             query:        Optional[str] = None):  # TODO add sorting parameter
    """
    Retrieve observations for the specified dataset.
    """
    dataset = JSONManager().get_dataset(json_id, dataset_name)

    def condition(row: Row):
        if query is None:
            return True
        return queryparser.parse(query, dataset.variables)(row)

    observations = dataset.observations

    # Filter and pagination on the same loop for performance
    result = []
    in_page, prev_in_page = False, False
    page_index = 0
    for obs in observations:
        in_page = math.floor(page_index / page_size) == page

        if not in_page and prev_in_page:
            break  # Break early

        if condition(obs):
            prev_in_page = in_page
            page_index += 1
            if in_page:
                result.append(obs)

    return result
