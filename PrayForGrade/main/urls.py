from django.urls import path
from main.views import home, detail, new_post

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>',detail, name="detail"),
    path('new_post/', new_post),
]