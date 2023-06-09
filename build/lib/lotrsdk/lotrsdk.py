import requests


class LotrSDK:
    def __init__(self, base_url='https://the-one-api.dev/v2', api_key=None):
        """
        Initializes the LotrSDK class.

        Parameters:
           base_url (str): The base URL of the API. Defaults to 'https://the-one-api.dev/v2'.
           api_key (str): Your API key. Defaults to None.

        Example:
           lotrsdk = LotrSDK(api_key='your_api_key')
        """
        self.base_url = base_url
        self.api_key = api_key

    def get_movies(self, **kwargs):
        """
        Retrieves movies from the API.

        Parameters:
           **kwargs: Arbitrary keyword arguments for API request.

        Returns:
           dict: A dictionary containing the API response.

        Example:
           movies = lotrsdk.get_movies()
           movies = lotrsdk.get_movies(sort='name:asc', runtimeInMinutes=('>=', 90))
        """
        return self._make_request('movie', kwargs)

    def get_movie(self, movie_id):
        """
        Retrieves a specific movie from the API.

        Parameters:
           movie_id (str): The id of the movie.

        Returns:
           dict: A dictionary containing the API response.

        Example:
           movie = lotrsdk.get_movie('5cd95395de30eff6ebccde5d')
        """
        return self._make_request(f'movie/{movie_id}')

    def get_movie_quotes(self, movie_id):
        """
        Retrieves quotes for a specific movie from the API.

        Parameters:
           movie_id (str): The id of the movie.

        Returns:
           dict: A dictionary containing the API response.

        Example:
           movie_quotes = lotrsdk.get_movie_quotes('5cd95395de30eff6ebccde5d')
        """
        return self._make_request(f'movie/{movie_id}/quote')

    def get_quotes(self, **kwargs):
        """
        Retrieves quotes from the API.

        Parameters:
           **kwargs: Arbitrary keyword arguments for API request.

        Returns:
           dict: A dictionary containing the API response.

        Example:
           quotes = lotrsdk.get_quotes()
           quotes = lotrsdk.get_quotes(character='Gandalf', limit=5, sort='dialog:asc')
        """
        return self._make_request('quote', kwargs)

    def get_quote(self, quote_id):
        """
        Retrieves a specific quote from the API.

        Parameters:
           quote_id (str): The id of the quote.

        Returns:
           dict: A dictionary containing the API response.

        Example:
           quote = lotrsdk.get_quote('5cd96e05de30eff6ebccebd0')
        """
        return self._make_request(f'quote/{quote_id}')

    def _make_request(self, endpoint, kwargs=None):
        """
        Makes a request to the API and returns the response.

        Parameters:
           endpoint (str): The API endpoint.
           kwargs (dict): A dictionary of keyword arguments for the API request.

        Returns:
           dict: A dictionary containing the API response.

        Raises:
           HTTPError: If an HTTP error occurs.

        Note: This function is for internal use and should not be called directly.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        params = []
        if kwargs:
            for key, value in kwargs.items():
                if isinstance(value, tuple) and len(value) == 2:
                    operator, val = value
                    params.append(f'{key}{operator}{val}')
                elif value == 'filtering_exists':
                    params.append(f'{key}')
                elif value == 'filtering_not_exists':
                    params.append(f'!{key}')
                else:
                    params.append(f'{key}={value}')
        if params:
            url += '?' + '&'.join(params)

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            raise Exception(f"HTTP Error: {err}") from err
        except requests.exceptions.ConnectionError as err:
            raise Exception(f"Connection Error: {err}") from err
        except requests.exceptions.Timeout as err:
            raise Exception(f"Timeout Error: {err}") from err
        except requests.exceptions.RequestException as err:
            raise Exception(f"Something went wrong: {err}") from err