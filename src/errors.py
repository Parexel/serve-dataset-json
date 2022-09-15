from http.client import BAD_REQUEST, NOT_FOUND


class HttpError(Exception):
    def __init__(self, code: int, msg: str):
        self._code = code
        super().__init__(msg)


class FilePathNotFound(HttpError):
    def __init__(self, file_path: str):
        super().__init__(NOT_FOUND, f"The given file path: {file_path} was not found.")


class JSONIDNotFound(HttpError):
    def __init__(self, id: int):
        super().__init__(NOT_FOUND, f"No json file was found for the given id: {id}")


class JSONFileAlreadyOpen(HttpError):
    def __init__(self, file_path: str):
        super().__init__(BAD_REQUEST, f"The given Dataset JSON file at: {file_path} is already open.")
