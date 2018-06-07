from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.add_new_text, name='add_new_text'),
    url(r'^add_new_text$', views.add_new_text, name='add_new_text'),
    url(r'^list_of_notes$', views.list_of_notes, name='list_of_notes'),
]