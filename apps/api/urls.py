
from django.urls import path
from .views import health
from .apps import MAJOR_VERSION


API_VERSION = f'v{MAJOR_VERSION}'

urlpatterns = [
    path(f'{API_VERSION}/health/', health),
]
