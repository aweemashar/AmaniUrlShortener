# URL Shortening Service

This is a URL shortening service built using Python and the Django framework. It allows users to create shortened URLs from the original ones and retrieve the original URL using the generated shortened URL.
In this we are using **pyshorteners** [documentation](https://pyshorteners.readthedocs.io/en/latest/) a python library to prepare unique short urls.

## Requirements

- Python 3.x
- Django
- Django Rest Framework (preferred)
- Docker
- Docker Compose

## Getting Started
1- Clone the repository.
   git clone https://github.com/yourusername/your-url-shortener.git
   
API Endpoints

**Create Shortened URL**

Endpoint: /urlshortener/create_short_url/

Method: POST

Request Payload:
{
  "url": "https://gist.github.com/ahmad-amaniai/19d8f7e5c12cc2c4a3164b7c8da7c224"
}

Response:
{
  "url": "https://tinyurl.com/ywqgzlmq"
}

**Retrieve Original URL**
Endpoint: /urlshortener/get_original_url/<shortened_url>/

Method: GET
Response:

Response:
{
  "url": "https://tinyurl.com/ywqgzlmq"
}
