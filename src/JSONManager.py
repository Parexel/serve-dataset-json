import src.utils as utils
import src.errors as errors
import os
import streamdatasetjson as dj


class JSONManager(metaclass=utils.SingletonMeta):
    def __init__(self):
        self._file_id_counter = 1
        self._open_jsons = {}
        self._open_datasets = {}

    def open(self, path: str) -> int:
        """
        Open DatasetJSON file.
        """
        if not os.path.exists(path):
            raise errors.FilePathNotFound(path)

        if self._path_is_open(path):
            raise errors.JSONFileAlreadyOpen(path)

        # TODO: raise error if the given file is an invalid Dataset JSON.
        json = dj.DatasetJSON(path)

        file_name = os.path.basename(path)
        new_id = self._get_new_id()
        self._open_jsons[new_id] = {"name": file_name, "path": path, "json": json}
        return new_id

    def close(self, json_id: int):
        """
        Close DatasetJSON file.
        """
        self.get(json_id).close()
        del self._open_jsons[json_id]
        self._open_datasets.pop(json_id, None)  # Removes key if present

    def get(self, json_id: int) -> dj.DatasetJSON:
        """
        Get open DatasetJSON instance by ID.
        """
        if not self._json_is_open(json_id):
            raise errors.JSONIDNotFound(json_id)

        return self._open_jsons[json_id]["json"]

    def get_dataset(self, json_id: int, name: str) -> dj.Dataset:
        self._lazy_load_dataset(json_id, name)
        return self._open_datasets[json_id][name]

    def available_jsons(self) -> dict:
        return {id: {"name": json_data["name"], "path": json_data["path"]}
                for id, json_data in self._open_jsons.items()}

    def dataset_metadata(self, json_id: int, name: str) -> dict:
        dataset = self.get_dataset(json_id, name)
        return dict({
            "name":    dataset.name,
            "label":   dataset.label,
            "records": dataset.records,
            "items":   [item._asdict() for item in dataset.items]
        })

    def _get_new_id(self) -> int:
        new_id = self._file_id_counter
        self._file_id_counter += 1
        return new_id

    def _path_is_open(self, path: str) -> bool:
        return path in [json_data["path"] for json_data in self.available_jsons().values()]

    def _json_is_open(self, json_id: int) -> bool:
        return json_id in self._open_jsons.keys()

    def _dataset_is_open(self, json_id: int, dataset_name: str) -> bool:
        return dataset_name in self._open_datasets.get(json_id, {}).keys()

    def _lazy_load_dataset(self, json_id: int, name: str):
        # Caché dataset
        if not self._dataset_is_open(json_id, name):
            try:
                dataset = self.get(json_id).get_dataset(name)
            except dj.DatasetNotFoundError:
                raise errors.DatasetNotInJSON(json_id, name)

            self._open_datasets[json_id] = self._open_datasets.get(json_id, {})
            self._open_datasets[json_id][name] = dataset
