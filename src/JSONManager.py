import utils
import errors
import os


class JSONManager(metaclass=utils.SingletonMeta):
    def __init__(self):
        self._file_id_counter = 1
        self._open_jsons = {}

    def open_json(self, path):
        if not os.path.exists(path):
            raise errors.FilePathNotFound(path)

        # TODO: raise error if the given file is an invalid Dataset JSON.

        file_name = os.path.basename(path)
        new_id = self._get_new_id()
        # TODO change "json": None to DatasetJSON object.
        self._open_jsons[new_id] = {"name": file_name, "path": path, "json": None}
        return new_id

    def close_json(self, id):
        if id not in self._open_jsons.keys():
            raise errors.JSONIDNotFound(id)

        self._open_jsons[id].close()
        del self._open_jsons[id]

    def available_jsons(self):
        return {id: {"name": json_data["name"], "path": json_data["path"]} for id, json_data in self._open_jsons}

    def _get_new_id(self):
        new_id = self._file_id_counter
        self._file_id_counter += 1
        return new_id
