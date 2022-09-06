from fastapi import FastAPI


app = FastAPI()


@app.get("/jsons")
async def get_all_jsons():
    """
    Retrieve all available DatasetJSON files.
    """
    return []


@app.get("/jsons/{file_name}/datasets")
async def get_all_datasets(file_name: str):
    """
    Retrieve all available Datasets for a given DatasetJSON.
    """
    return []


@app.get("/jsons/{file_name}/datasets/{dataset_name}/metadata")
async def get_dataset_metadata(file_name: str, dataset_name: str):
    """
    Retrieve metadata for the specified dataset.
    """
    return {}


@app.get("/jsons/{file_name}/datasets/{dataset_name}/observations")
async def get_dataset_observations(file_name: str, dataset_name: str):
    """
    Retrieve observations for the specified dataset.
    TODO: Add parameters for filtering and paginating the data.
    """
    return []