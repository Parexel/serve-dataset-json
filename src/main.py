import math
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
                             page:         Optional[int],
                             page_size:    Optional[int],
                             query:        Optional[str]):  # TODO add sorting parameter
    """
    Retrieve observations for the specified dataset.
    """
    def condition(_): return True  # TODO replace with query parser
    observations = JSONManager().get_dataset(json_id, dataset_name).observations

    result = []
    prev_in_page = False
    in_page = False
    for i, obs in enumerate(observations):
        prev_in_page = in_page
        in_page = math.ceil(i / page_size) == page
        if in_page and condition(obs):
            result.append(obs)
        elif prev_in_page:
            break  # Break early

    return result
