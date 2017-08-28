from django.conf.urls import url
from primera.views import index,persist,ConsultarBaseDatos


urlpatterns = [
    url(r'^$', index),
    url(r'^primera$',index),
    url(r'^input-to-database$',persist,name='persist'),
    url(r'^consultar-bd$',ConsultarBaseDatos,name='consultar'),



]

