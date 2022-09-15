from fastapi import HTTPException
from http.client import BAD_REQUEST, NOT_FOUND


class FilePathNotFound(HTTPException):
    def __init__(self, file_path: str):
        super().__init__(status_code=NOT_FOUND,
                         detail=f"The given file path: {file_path} was not found.")


class JSONIDNotFound(HTTPException):
    def __init__(self, id: int):
        super().__init__(status_code=NOT_FOUND,
                         detail=f"No json file was found for the given id: {id}")


class JSONFileAlreadyOpen(HTTPException):
    def __init__(self, file_path: str):
        super().__init__(status_code=BAD_REQUEST,
                         detail=f"The given Dataset JSON file at: {file_path} is already open.")
