from django.urls import path
from .views import IndexView ,LeiamaisView
urlpatterns = [

    path('',IndexView.as_view(), name='index'),
    path('leiamais/', LeiamaisView.as_view(), name='leiamais')

]