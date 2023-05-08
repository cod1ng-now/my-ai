from django.shortcuts import render
import openai, requests
from django.core.files.base import ContentFile
from .models import Image
api_key = "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"
openai.api_key = api_key
def generate_image_from_txt(request):
    obj = None
    if api_key is not None and request.method =='POST':
        user_input = request.POST.get('user_input')
        response = openai.Image.create(
            prompt=user_input,
            size="512x512"
        )
        img_url = response['data'][0]['url']
        response = requests.get(img_url)
        image_file=  ContentFile(response.content)
        
        
        count = Image.objects.count() + 1
        fname = f"Image-{count}.jpg"
        obj = Image(pharse=user_input)
        obj.ai_image.save(fname, image_file)
        obj.save()
    return render(request, 'main.html', {"object":obj})