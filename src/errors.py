from http.client import NOT_FOUND


class HttpError(Exception):
    def __init__(self, code, msg):
        self._code = code
        super().__init__(msg)


class FilePathNotFound(HttpError):
    def __init__(self, file_path):
        super().__init__(NOT_FOUND, f"The given file path: {file_path} was not found.")


class JSONIDNotFound(HttpError):
    def __init__(self, id):
        super().__init__(NOT_FOUND, f"No json file was found for the given id: {id}")
