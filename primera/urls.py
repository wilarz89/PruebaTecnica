from django.conf.urls import url
from primera.views import index,persist


urlpatterns = [
    url(r'^$', index),
    url(r'^primera$',index),
    url(r'^input-to-database$',persist,name='persist'),



]

