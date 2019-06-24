from django.conf.urls import url

from li import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
]