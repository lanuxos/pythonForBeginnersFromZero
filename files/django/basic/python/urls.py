from django.urls import path
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls)
    path('', hello),
    path('home/', homepage, name='home-page'),
    path('contact/', contactpage, name='contact-page'),
]
