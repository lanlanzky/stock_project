from django.conf.urls import patterns, include, url
from stock_project.views import *
from cluster.views import cluster
from learning_machine.views import *
from news.views import *
from django.contrib import admin
#admin.autodiscover()#find admin.py
urlpatterns = patterns('',
          (r'^$',index),
	 # (r'', include(admin.site.urls)),
          (r'^method$',method),
          (r'^stock$',stock),
          (r'^information$',information),
          (r'^cluster$',cluster),
          (r'^home$',index),
          (r'^search/$',search),
          (r'^bigdata/$',bigdata),
#     (r'^test/$',test),
         # (r'^search-form/$', search_form),
	 )
                                                                  # (r'^about/(\w+)/$', about_pages),)
