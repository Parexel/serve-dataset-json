import unittest

import src.queryparser as queryparser


class TestVariableVsLiteralConditions(unittest.TestCase):
    exampleVars = ["NAME", "AGE"]

    def test_equals_for_number_true(self):
        query = "AGE == 24"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(["Juan", 24]))

    def test_equals_for_number_false(self):
        query = "AGE == 10"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(["Juan", 24]))

    def test_equals_for_string_true(self):
        query = 'NAME == "Juan"'
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(["Juan", 24]))

    def test_equals_for_string_false(self):
        query = "NAME == \"Ivan\""
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(["Juan", 24]))


class TestLiteralVsLiteralConditions(unittest.TestCase):
    exampleVars = ["NAME", "AGE"]
    exampleObs = ["Juan", 24]

    def test_literal_number_equals_true(self):
        query = "1 == 1"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_number_equals_false(self):
        query = "1 == 2"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))

    def test_literal_string_equals_true(self):
        query = '"hola" == "hola"'
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_string_equals_false(self):
        query = '"hola" == "chau"'
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))

    def test_literal_number_not_equal_true(self):
        query = "1 != 2"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_number_not_equal_false(self):
        query = "1 != 1"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))

    def test_literal_string_not_equal_true(self):
        query = '"hola" != "chau"'
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_string_not_equal_false(self):
        query = '"hola" != "hola"'
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))

    def test_literal_number_greater_than_true(self):
        query = "1 > 0"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_number_greater_than_false(self):
        query = "0 > 1"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))

    def test_literal_number_greater_than_or_equal_true(self):
        query = "1 >= 0"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_number_greater_than_or_equal_false(self):
        query = "0 >= 1"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))

    def test_literal_number_less_than_true(self):
        query = "1 < 2"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_number_less_than_false(self):
        query = "2 < 1"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))

    def test_literal_number_less_than_or_equal_true(self):
        query = "0 <= 1"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertTrue(condition(self.exampleObs))

    def test_literal_number_less_than_or_equal_false(self):
        query = "2 <= 1"
        condition = queryparser.parse(query, self.exampleVars)
        self.assertFalse(condition(self.exampleObs))
