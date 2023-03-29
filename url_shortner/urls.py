from django.urls import path

from url_shortner.views import URLShortnerCreateView, VerifiedPasswordView

urlpatterns = [
    path('', URLShortnerCreateView.as_view(), name='home_page'),
    path('verify-password/<str:short_url>/', VerifiedPasswordView.as_view(), name='verify_password')
]
