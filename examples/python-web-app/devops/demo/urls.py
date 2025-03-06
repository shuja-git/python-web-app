from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# from django.contrib import admin
# from django.urls import path, include
# from django.http import HttpResponse

# # Create a simple home page response
# def home(request):
#     return HttpResponse("Welcome to the homepage!")

# urlpatterns = [
#     path('', home),  # Add this line to handle requests to "/"
#     path('demo/', include('demo.urls')),  # Existing route
#     path('admin/', admin.site.urls),  # Admin panel
# ]
