# Solution

## To build and upload 

```bash
$ python -m pip install setuptools wheel
$ python setup.py sdist bdist_wheel
$ python -m pip install twine
$ python -m twine upload -r testpypi dist/*
```

## To install 

```bash
$ python -m pip install -i https://test.pypi.org/simple/ lotr-sdk-sachiketha==0.0.1
```

## To Test 

1. `/movie`

```python
from lotrsdk import LotrSDK
lotrsdk = LotrSDK(api_key='apikey')
lotrsdk.get_movies()
```

2. `/movie/{id}`

```python
from lotrsdk import LotrSDK
lotrsdk = LotrSDK(api_key='apikey')
lotrsdk.get_movie('movie_id')
```

3. `/movie/{id}/quote`

```python
from lotrsdk import LotrSDK
lotrsdk = LotrSDK(api_key='apikey')
lotrsdk.get_movie_quotes('movie_id')
```

4. `/quote`

```python
from lotrsdk import LotrSDK
lotrsdk = LotrSDK(api_key='apikey')
lotrsdk.get_quotes()
```

5. `/quote/{id}`

```python
from lotrsdk import LotrSDK
lotrsdk = LotrSDK(api_key='apikey')
lotrsdk.get_quote('quote_id')
```

## To run unit tests

```bash
$ python -m unittest lotrsdk_tests.py
```