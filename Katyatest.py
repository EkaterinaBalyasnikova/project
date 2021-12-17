import unittest

from main import validation

class ProjectTest(unittest.TestCase):

    def test_validation_up_true(self):
        self.assertTrue(validation('w', [
            ' 1', ' 2', ' 3', ' 4', ' 5',
            ' 6', '  ', ' 8', ' 9', ' 10',
            ' 11', '12', '13', '14', ' 15',
            ' 16', '17', '18', '19', ' 20',
            '21', '22', '23', '24', ' 7']))

    def test_validation_down_true(self):
        self.assertTrue(validation('s', [
            ' 1', ' 2', ' 3', ' 4', ' 5',
            ' 6', ' 7 ', ' 8', ' 9', ' 10',
            ' 11', '12', '13', '14', ' 15',
            ' 16', '17', '18', '19', ' 20',
            '21', '22', '23', '24', ' ']))

    def test_validation_left_true(self):
        self.assertTrue(validation('a', [
            ' 1', ' 2', ' 3', ' 4', ' 5',
            ' 6', ' 7 ', ' ', ' 9', ' 10',
            ' 11', '12', '13', '14', ' 15',
            ' 16', '17', '18', '19', ' 20',
            '21', '22', '23', '24', ' 8']))

    def test_validation_right_true(self):
        self.assertTrue(validation('d', [
            ' 1', ' 2', ' 3', ' 4', ' 5',
            ' 6', ' 7 ', ' 8', ' 9', ' 10',
            ' 11', '12', '13', '14', ' 15',
            ' 16', '17', '18', '19', ' 20',
            '21', '22', '23', '24', ' ']))

    def test_validationt_up_false(self):
        self.assertFalse(validation('w', [
            ' 1', ' 2', ' 3', ' 4', ' 5',
            ' 6', ' 7 ', ' 8', ' 9', ' 10',
            ' 11', '12', '13', '14', ' 15',
            ' 16', '17', '18', '19', ' 20',
            '21', '22', '23', '24', ' ']))

    def test_validation_down_false(self):
        self.assertFalse(validation('s', [
            ' ', ' 2', ' 3', ' 4', ' 5',
            ' 6', ' 7 ', ' 8', ' 9', ' 10',
            ' 11', '12', '13', '14', ' 15',
            ' 16', '17', '18', '19', ' 20',
            '21', '22', '23', '24', '1']))

    def test_validation_left_false(self):
        self.assertFalse(validation('a', [
            ' 1', ' 2', ' 3', ' 4', ' 5',
            ' 6', ' 7 ', ' 8', ' 9', ' 10',
            ' 11', '12', '13', '14', ' 15',
            ' 16', '17', '18', '19', ' 20',
            '21', '22', '23', '24', ' ']))

    def test_validation_right_false(self):
        self.assertFalse(validation('d', [
            ' ', ' 2', ' 3', ' 4', ' 5',
            ' 6', ' 7 ', ' 8', ' 9', ' 10',
            ' 11', '12', '13', '14', ' 15',
            ' 16', '17', '18', '19', ' 20',
            '21', '22', '23', '24', '1']))
