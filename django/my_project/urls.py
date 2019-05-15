from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from django.http import HttpResponse


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


images = {}


def fractal_request_handler(request):
    import os, re
    os.system('cd ../python_app && docker-compose build --build-arg args="{}" app && docker-compose up -d'.format(
        request.body.decode("utf-8").replace("\"", "'").replace(' ', '')
    ))
    return HttpResponse('Fractal requested')


def results_handler(request):
    import json
    data = json.loads(request.body.decode("utf-8"))
    images[data['name']] = data['image']
    return HttpResponse('Fractal collected')


def image_preview(request):
    import base64
    # import json
    # print(request.GET['name'])
    # data = json.loads(request.params.decode("utf-8"))
    imgstring = images[request.GET['name']]
    image_64_decode = base64.b64decode(imgstring)
    return HttpResponse(image_64_decode, content_type="image/png")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('fractal/', fractal_request_handler),
    path('results/', results_handler),
    path('preview/', image_preview),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
