# Import admin module
from django.contrib import admin

# Import path module
from django.urls import path

# Import view
from searchapp import views

# Define paths
urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.default, name='default'),
     path('search/', views.search, name='search'),
]