from django.urls import path
from .views import generate_image_from_txt
urlpatterns = [
    path('', generate_image_from_txt)
]
