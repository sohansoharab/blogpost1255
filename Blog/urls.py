from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('post_detail/<int:pk>', views.PostDetails.as_view(), name='post_detail'),
]
