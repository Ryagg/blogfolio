from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('site_notice/', views.SiteNoticeView.as_view(), name='site_notice'),
    path('privacy_policy/', views.PrivacyPolicyView.as_view(), name='privacy_policy'),
]
