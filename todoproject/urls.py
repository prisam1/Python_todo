from django.contrib import admin
from django.urls import path, include
from todoapp import views

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', include('todoapp.urls')),
    path('',  include('todoapp.urls')),
    path('',  include('todoapp.urls')),
    path('',  include('todoapp.urls')),
]   