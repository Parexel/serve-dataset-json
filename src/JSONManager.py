import utils
import errors
import os


class JSONManager(metaclass=utils.SingletonMeta):
    def __init__(self):
        self._file_id_counter = 1
        self._json_files = {}
    
    def register_json(self, path):
        if not os.path.exists(path):
            raise errors.FilePathNotFound(path)

        # TODO: raise error if the given file is an invalid Dataset JSON.
        
        file_name = os.path.basename(path)
        new_id = self._get_new_id()
        self._json_files[new_id] = { "name": file_name, "path": path }
        return new_id

    def get_json_path(self, id):
        if id not in self._json_files.keys():
            raise errors.JSONIDNotFound(id)

        return self._json_files[id]["path"]

    def available_jsons(self):
        return self._json_files

    def _get_new_id(self):
        new_id = self._file_id_counter
        self._file_id_counter += 1
        return new_id