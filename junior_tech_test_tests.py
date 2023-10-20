# test_data_processing.py

import unittest
from junior_tech_test import *

class TestDataProcessing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = read_csv_file('sample_data.csv')

    def test_get_unique_teams(self):
        result = get_unique_teams(self.data)
        self.assertEqual(result, {'Germany', 'Costa Rica'})

    def test_get_most_common_event_type(self):
        result = get_most_common_event_type(self.data)
        self.assertEqual(result, 'Pass')

    def test_filter_by_team(self):
        result = filter_by_team(self.data, 'Germany')
        self.assertTrue(all(row['team_name'] == 'Germany' for row in result))

    def test_count_event_type_by_team(self):
        result = count_event_type_by_team(self.data, 'Germany', 'Pass')
        self.assertEqual(result, 766)

    def test_average_pass_length_by_team(self):
        result = average_pass_length_by_team(self.data, 'Germany')
        self.assertAlmostEqual(result, 19.8, places=6)

    def test_filter_players_by_position(self):
        result = filter_players_by_position(self.data, 'Center Forward')
        self.assertEqual(result, set(['Johan Alberto Venegas Ulloa','Thomas Müller','Joel Nathaniel Campbell Samuels']))

    def test_count_successful_passes(self):
        result = count_successful_passes(self.data)
        self.assertEqual(result, 953)

    def test_filter_by_period(self):
        result = filter_by_period(self.data, '1')
        self.assertTrue(all(row['period'] == '1' for row in result))

    def test_count_shots_by_player(self):
        result = count_shots_by_player(self.data, 'Thomas Müller')
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
