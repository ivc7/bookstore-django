from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.store, name='index'),
    url(r'^book/(\d+)',views.book_detail,name='book_details')
]
