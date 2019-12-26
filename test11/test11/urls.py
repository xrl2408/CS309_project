"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web1 import views
from django.conf.urls import url
urlpatterns = [
   path('admin/', admin.site.urls),
url(r'^index/',views.index),
url(r'^search/',views.search),
url(r'^add_page/',views.add_page),
url(r'^change_/',views.change_),
url(r'^D/',views.D),
url(r'^login/', views.login),
url(r'^register/', views.register),
url(r'^logout/', views.logout),
url(r'^back/', views.back),
url(r'^log/', views.log),
url(r'^log_b/', views.log_b),
url(r'^D_b/', views.D_b),
url(r'^Change_b/', views.Change_b),
url(r'^show/', views.show),
url(r'^test_for_c/',views.test_for_c),
url(r'^search1/',views.search1),
url(r'^change_1/',views.change_1),
url(r'^download/',views.download),
url(r'^index_test/',views.index_test),
url(r'^index_QA/',views.index_QA),
url(r'^QA_action/',views.QA_action),
url(r'^QA_add/',views.QA_add),
url(r'^QA_show_one/',views.QA_show_one),
url(r'^QA_anwser/',views.QA_answer),
url(r'^QA_show_anwsers/',views.QA_show_anwsers),
url(r'^QA_anwsers_one/',views.QA_anwsers_one),
url(r'^download_in_one/',views.download_in_one),
url(r'^Coures_show/',views.Coures_show),
url(r'^Q_D/',views.Q_D),
url(r'^Q_A_D/',views.Q_A_D),

   ]
