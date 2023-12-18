# yoga_api/urls.py

from django.urls import path
from .views import EnrollUserView

urlpatterns = [
    path('enroll/', EnrollUserView.as_view(), name='enroll-user'),
]
