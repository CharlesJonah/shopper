from django.conf.urls import url
from . import views

app_name = 'shop'
urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^$', views.home, name='home'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^profile/$', views.profile, name='profile'),
]