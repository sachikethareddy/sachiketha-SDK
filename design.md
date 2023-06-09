# Design of the Lord of the Rings SDK

## Architecture

The SDK is designed around a central `LotrSDK` class, which manages all interactions with the API. This class provides methods for making requests to various endpoints, such as `get_movies`, `get_movie`, `get_movie_quotes`, `get_quotes`, and `get_quote`. 

These methods accept a variety of arguments, allowing users to specify query parameters in a simple and intuitive way. For example, users can pass in filters as keyword arguments, which are automatically converted into the appropriate query string.

## Testing

The SDK includes a suite of unit tests, which mock the API responses using the `requests_mock` library. This allows us to test the functionality of the SDK without making actual requests to the API.

## Documentation

All methods in the `LotrSDK` class are documented with docstrings, providing information on the method's purpose, its arguments, and its return value. These docstrings follow the Google Python Style Guide.

The SDK also includes a README file, which provides a high-level overview of the SDK's functionality, as well as examples of how to use each method.
