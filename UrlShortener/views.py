from django.http import JsonResponse
from UrlShortener.models import URLS
from rest_framework.decorators import api_view
import pyshorteners
from UrlShortener.form import CreateShortURLForm

# Create your views here.


@api_view(['POST'])
def create_short_url(request):
    form = CreateShortURLForm(request.data)
    if form.is_valid():
        url = form.data['url']

        # Check if the URL already exists
        url_object = URLS.objects.filter(original_url=url).first()
        if url_object:
            return JsonResponse({"url": url_object.shorten_url}, status=200)

        # If it doesn't exist, generate a new object in  URLS model
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(url)
        urls = URLS(shorten_url=short_url, original_url=url)
        urls.save()
        return JsonResponse({"url": short_url}, status=200)

    else:
        return JsonResponse({"error": "Invalid/Missing Data"}, status=400)


@api_view(['GET'])
def get_original_url(request, url):

    # Check if the URL exists
    url_object = URLS.objects.filter(shorten_url=url).first()
    if url_object:
        return JsonResponse({"url": url_object.original_url})

    else:
        return JsonResponse({"message": "URL Does Not Exist"}, status=200)



