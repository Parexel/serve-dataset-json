import unittest

import src.queryparser as queryparser


class TestLiteralConditions(unittest.TestCase):
    exampleVars = ["NAME", "AGE"]
    exampleObs = ["Juan", 24]

    def test_literal_number_equivalence_tautology(self):
        query = "1 == 1"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_number_equivalence_fallacy(self):
        query = "1 == 2"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))

    def test_literal_string_equivalence_tautology(self):
        query = "\"hola\" == \"hola\""
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_string_equivalence_fallacy(self):
        query = "\"hola\" == \"chau\""
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))

    def test_literal_number_not_equal_tautology(self):
        query = "1 != 2"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_number_not_equal_fallacy(self):
        query = "1 != 1"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))

    def test_literal_string_not_equal_tautology(self):
        query = "\"hola\" != \"chau\""
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_string_not_equal_fallacy(self):
        query = "\"hola\" != \"hola\""
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))

    def test_literal_number_greater_than_tautology(self):
        query = "1 > 0"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_number_greater_than_fallacy(self):
        query = "0 > 1"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))

    def test_literal_number_greater_than_or_equal_tautology(self):
        query = "1 >= 0"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_number_greater_than_or_equal_fallacy(self):
        query = "0 >= 1"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))
    
    def test_literal_number_less_than_tautology(self):
        query = "1 < 2"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_number_less_than_fallacy(self):
        query = "2 < 1"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))

    def test_literal_number_less_than_or_equal_tautology(self):
        query = "0 <= 1"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_number_less_than_or_equal_fallacy(self):
        query = "2 <= 1"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))