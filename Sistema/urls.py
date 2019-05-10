from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import registroCliente

urlpatterns=[
    url(r'^$',views.inicio,name="inicio"),
    url(r'^registro/$',views.registroCliente,name="registroCliente"),
    url(r'^login/',views.loginCliente,name="login"),
	url(r'^logout/', views.logoutCliente, name="logout"),

]

urlpatterns += staticfiles_urlpatterns()