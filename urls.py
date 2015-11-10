from django.conf.urls.defaults import patterns, include, url
from ge import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.search_form),
    (r'^summary/$',views.summary),
    (r'^add_form/$',views.add_form),
    (r'^add_result/$',views.add_result),
    (r'^search_result/$', views.search_result),
    (r'^search_result/delete/$', views.delete),
    (r'^search_result/information/$', views.information),
    
    # Examples:
    # url(r'^$', 'shuai.views.home', name='home'),
    # url(r'^shuai/', include('shuai.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
