import utils
import errors
import os


class JSONManager(metaclass=utils.SingletonMeta):
    def __init__(self):
        self._file_id_counter = 1
        self._open_jsons = {}
        self._open_datasets = {}

    def open_json(self, path: str) -> int:
        if not os.path.exists(path):
            raise errors.FilePathNotFound(path)

        if self._path_is_open(path):
            raise errors.JSONFileAlreadyOpen(path)

        # TODO: raise error if the given file is an invalid Dataset JSON.

        file_name = os.path.basename(path)
        new_id = self._get_new_id()
        # TODO change "json": None to the instanced DatasetJSON object.
        self._open_jsons[new_id] = {"name": file_name, "path": path, "json": None}
        return new_id

    def get_dataset(self, json_id: int, name: str):
        self._lazy_load_dataset(json_id, name)
        return self._open_datasets[json_id][name]

    def close_json(self, json_id: int):
        if not self._json_is_open(json_id):
            raise errors.JSONIDNotFound(json_id)

        self._open_jsons[json_id].close()
        del self._open_jsons[json_id]
        del self._open_datasets[json_id]

    def available_jsons(self) -> dict:
        return {id: {"name": json_data["name"], "path": json_data["path"]} for id, json_data in self._open_jsons}

    def _get_new_id(self) -> int:
        new_id = self._file_id_counter
        self._file_id_counter += 1
        return new_id

    def _path_is_open(self, path: str) -> bool:
        return path in [json_data["path"] for json_data in self.available_jsons().values()]

    def _json_is_open(self, json_id: int) -> bool:
        return json_id in self._open_jsons.keys()

    def _dataset_is_open(self, json_id: int, dataset_name: str) -> bool:
        return dataset_name in self._open_datasets[json_id].keys()

    # This method is not exposed because it shouldn't be used outside this class.
    # get_dataset is the method that should be used.
    def _lazy_load_dataset(self, json_id: int, name: str):
        if not self._json_is_open(json_id):
            raise errors.JSONIDNotFound(json_id)

        # Caché dataset
        if not self._dataset_is_open(json_id, name):
            try:
                dataset = None  # TODO json.get_dataset(name)
                self._open_datasets[json_id][name] = dataset
            except Exception:  # TODO catch the specific exception
                raise errors.DatasetNotInJSON(json_id, name)
