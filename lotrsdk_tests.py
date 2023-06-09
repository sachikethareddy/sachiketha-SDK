import os
import json
import unittest
from unittest.mock import patch
from lotrsdk.lotrsdk import LotrSDK


class TestClient(unittest.TestCase):

    def setUp(self):
        self.lotrsdk = LotrSDK(api_key='your-api-key')
        self.endpoint = 'https://the-one-api.dev/v2/'
        self.headers = {'Authorization': 'Bearer your-api-key'}
        mock_data_movies_path = os.path.join(os.path.dirname(__file__), 'movies.json')
        with open(mock_data_movies_path, 'r') as f:
            self.mock_data_movies = json.load(f)

        mock_data_quotes_path = os.path.join(os.path.dirname(__file__), 'quotes.json')
        with open(mock_data_quotes_path, 'r') as f:
            self.mock_data_quotes = json.load(f)

    @patch('requests.get')
    def test_get_movies(self, mock_get):
        mock_get.return_value.json.return_value = self.mock_data_movies
        response = self.lotrsdk.get_movies()
        mock_get.assert_called_once_with(f'{self.endpoint}movie', headers=self.headers)
        self.assertEqual(response, self.mock_data_movies)

    @patch('requests.get')
    def test_get_movie(self, mock_get):
        mock_get.return_value.json.return_value = self.mock_data_movies['docs'][0]
        response = self.lotrsdk.get_movie('5cd95395de30eff6ebccde56')
        mock_get.assert_called_once_with(f'{self.endpoint}movie/5cd95395de30eff6ebccde56',
                                         headers=self.headers)
        self.assertEqual(response, self.mock_data_movies['docs'][0])

    @patch('requests.get')
    def test_get_movies_with_budget_less_than_100(self, mock_get):
        mock_get.return_value.json.return_value = self.mock_data_movies
        response = self.lotrsdk.get_movies(budgetInMillions=('<', 100))
        mock_get.assert_called_once_with(f'{self.endpoint}movie?budgetInMillions<100',
                                         headers=self.headers)
        self.assertEqual(response, self.mock_data_movies)

    @patch('requests.get')
    def test_get_movies_with_awards_greater_than_0(self, mock_get):
        mock_get.return_value.json.return_value = self.mock_data_movies
        response = self.lotrsdk.get_movies(academyAwardWins=('>', 0))
        mock_get.assert_called_once_with(f'{self.endpoint}movie?academyAwardWins>0',
                                         headers=self.headers)
        self.assertEqual(response, self.mock_data_movies)

    @patch('requests.get')
    def test_get_movies_with_runtime_greater_than_or_equal_to_160(self, mock_get):
        mock_get.return_value.json.return_value = self.mock_data_movies
        response = self.lotrsdk.get_movies(runtimeInMinutes=('>=', 160))
        mock_get.assert_called_once_with(f'{self.endpoint}movie?runtimeInMinutes>=160',
                                         headers=self.headers)
        self.assertEqual(response, self.mock_data_movies)

    @patch('requests.get')
    def test_get_movies_by_sorting(self, mock_get):
        mock_get.return_value.json.return_value = self.mock_data_movies
        response = self.lotrsdk.get_movies(sort='name:asc')
        mock_get.assert_called_once_with(f'{self.endpoint}movie?sort=name:asc',
                                         headers=self.headers)
        self.assertEqual(response, self.mock_data_movies)

    @patch('requests.get')
    def test_get_movie_by_filtering(self, mock_get):
        mock_get.return_value.json.return_value = self.mock_data_movies
        response = self.lotrsdk.get_movies(name='/Ring/i')
        mock_get.assert_called_once_with(f'{self.endpoint}movie?name=/Ring/i', headers=self.headers)
        self.assertEqual(response, self.mock_data_movies)

    @patch('requests.get')
    def test_get_movie_quotes(self, mock_get):
        mock_get.return_value.json.return_value = self.mock_data_quotes
        response = self.lotrsdk.get_movie_quotes('5cd95395de30eff6ebccde5d')
        mock_get.assert_called_once_with(f'{self.endpoint}movie/5cd95395de30eff6ebccde5d/quote',
                                         headers=self.headers)
        self.assertEqual(response, self.mock_data_quotes)

    @patch('requests.get')
    def test_get_quotes(self, mock_get):
        mock_get.return_value.json.return_value = self.mock_data_quotes
        response = self.lotrsdk.get_quotes()
        mock_get.assert_called_once_with(f'{self.endpoint}quote', headers=self.headers)
        self.assertEqual(response, self.mock_data_quotes)

    @patch('requests.get')
    def test_get_quote(self, mock_get):
        mock_get.return_value.json.return_value = self.mock_data_quotes['docs'][0]
        response = self.lotrsdk.get_quote('5cd96e05de30eff6ebccebd0')
        mock_get.assert_called_once_with(f'{self.endpoint}quote/5cd96e05de30eff6ebccebd0',
                                         headers=self.headers)
        self.assertEqual(response, self.mock_data_quotes['docs'][0])

    @patch('requests.get')
    def test_get_quotes_by_pagination(self, mock_get):
        mock_get.return_value.json.return_value = self.mock_data_quotes
        response = self.lotrsdk.get_quotes(page=2, limit=10)
        mock_get.assert_called_once_with(f'{self.endpoint}quote?page=2&limit=10',
                                         headers=self.headers)
        self.assertEqual(response, self.mock_data_quotes)


if __name__ == '__main__':
    unittest.main()