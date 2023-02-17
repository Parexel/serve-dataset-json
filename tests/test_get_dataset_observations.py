import unittest

import src.main as main


class TestQueryParameter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example_json_id = main.open_json_path("./examples/adae.json")

    def test_observations_satisfy_specified_query(self):
        query = "USUBJID = \"01-701-1015\""
        obs = main.get_dataset_observations(self.example_json_id, "ADAE", page=1, page_size=100, query=query)
        self.assertTrue(all(map(lambda o: o[3] == "01-701-1015", obs)))

    def test_there_are_no_observations_that_do_not_satisfy_query(self):
        query = "AGEGR1N = 2"
        obs = main.get_dataset_observations(self.example_json_id, "ADAE", page=1, page_size=100, query=query)
        self.assertFalse(any(map(lambda o: o[8] != 2, obs)))
