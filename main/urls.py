from django.urls import path
from main.views import home, detail, new_post, detail_ajax

urlpatterns = [
    path('', home, name='home'),
    # path('detail/<int:pk>',detail, name="detail"),
    path('detail_ajax/<int:pk>',detail_ajax, name="detail_ajax"),
    path('new_post/', new_post),
]