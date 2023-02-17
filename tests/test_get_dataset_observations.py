import unittest
from src.JSONManager import JSONManager

import src.main as main


class TestQueryParameter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example_json_id = main.open_json_path("./examples/adae.json")

    def test_observations_satisfy_specified_query(self):
        query = "USUBJID = \"01-701-1015\""
        obs = main.get_dataset_observations(self.example_json_id, "ADAE", page=0, page_size=100, query=query)
        self.assertTrue(all(map(lambda o: o[3] == "01-701-1015", obs)))

    def test_there_are_no_observations_that_do_not_satisfy_query(self):
        query = "AGEGR1N = 2"
        obs = main.get_dataset_observations(self.example_json_id, "ADAE", page=0, page_size=100, query=query)
        self.assertFalse(any(map(lambda o: o[8] != 2, obs)))

    def test_correctly_retrieves_the_first_page(self):
        first_page = main.get_dataset_observations(self.example_json_id, "ADAE", page=0, page_size=10)
        total_observations = JSONManager().get_dataset(self.example_json_id, "ADAE").observations
        self.assertListEqual(first_page, list(total_observations)[:10])

    def test_correctly_retrieves_an_arbitrary_page(self):
        first_page = main.get_dataset_observations(self.example_json_id, "ADAE", page=2, page_size=5)
        total_observations = JSONManager().get_dataset(self.example_json_id, "ADAE").observations
        self.assertListEqual(first_page, list(total_observations)[10:15])
