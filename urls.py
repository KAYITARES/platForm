from django.contrib import admin
from django.conf.urls import url,include

urlspatterns=[
  url('^admin/',admin.site.urls),
  url('^news/',include('news.urls'))
]