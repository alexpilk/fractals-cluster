import django

django.views.decorators.csrf.csrf_protect = lambda x: x

from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os


class LopataResponse(HttpResponse):
    def __init__(self, data, then_callback, **kwargs):
        super().__init__(data, **kwargs)
        self.then_callback = then_callback

    def close(self):
        super().close()
        self.then_callback()


class RequestMonitor:
    MAX_PROCESSING_REQUESTS = 4
    PROCESSING_REQUESTS = 0
    REQUEST_QUEUE = []

    @classmethod
    def add_to_queue(cls, request):
        cls.REQUEST_QUEUE.append(request)

    @classmethod
    def take_from_queue(cls):
        return cls.REQUEST_QUEUE.pop(0)

    @classmethod
    def notify_about_new_request(cls):
        cls.PROCESSING_REQUESTS += 1

    @classmethod
    def notify_about_finishing_request(cls):
        cls.PROCESSING_REQUESTS -= 1

    @classmethod
    def busy(cls):
        return cls.PROCESSING_REQUESTS >= cls.MAX_PROCESSING_REQUESTS


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def _process_fractal_request(request_string):
    data = json.loads(request_string)
    os.system('cd ../python_app && docker-compose build --build-arg args="{}" app && docker-compose up -d'.format(
        request_string.replace("\"", "'").replace(' ', '')
    ))
    try:
        os.remove(data['user'])
    except OSError:
        pass
    return HttpResponse('Fractal requested')


def fractal_request_handler(request):
    request_string = request.body.decode("utf-8")
    if RequestMonitor.busy():
        RequestMonitor.add_to_queue(request_string)
        return HttpResponse('Fractal request put into queue')
    RequestMonitor.notify_about_new_request()
    return _process_fractal_request(request_string)


def _next_request_from_queue_callback():
    try:
        next_request = RequestMonitor.take_from_queue()
    except IndexError:
        pass
    else:
        _process_fractal_request(next_request)


def _load_image(user):
    with open(user) as image:
        return image.read()


def _save_image(user, image_content):
    with open(user, 'w+') as image:
        image.write(image_content)


def results_handler(request):
    RequestMonitor.notify_about_finishing_request()
    data = json.loads(request.body.decode("utf-8"))
    _save_image(data['user'], data['image'])
    return LopataResponse('Fractal collected', _next_request_from_queue_callback)


def image_preview(request):
    import base64
    imgstring = _load_image(request.GET['user'])
    image_64_decode = base64.b64decode(imgstring)
    return HttpResponse(image_64_decode, content_type="image/png")


def image_preview_base64(request):
    imgstring = _load_image(request.GET['user'])
    return HttpResponse(imgstring)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', csrf_exempt(LoginView.as_view()), name='login'),
    path('logout/', csrf_exempt(LogoutView.as_view()), name='logout'),
    path('signup/', csrf_exempt(SignUp.as_view()), name='signup'),
    path('fractal/', csrf_exempt(fractal_request_handler)),
    path('results/', csrf_exempt(results_handler)),
    path('preview/', csrf_exempt(image_preview)),
    path('preview64/', csrf_exempt(image_preview_base64)),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
