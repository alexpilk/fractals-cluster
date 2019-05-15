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


def fractal_request_handler(request):
    import os
    os.system('cd ../python_app && docker-compose build --build-arg args="{}" app && docker-compose up -d'.format(request.body))
    return HttpResponse('Fractal requested')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('fractal/', fractal_request_handler),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
