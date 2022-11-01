from django.urls import path
from .views import SignupView, UsercheckView, UserDataView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('usertype/', UsercheckView.as_view()),
    path('userdata/', UserDataView.as_view()),
]
