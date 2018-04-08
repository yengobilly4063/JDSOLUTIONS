from django.conf.urls import url
from . import views







urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'^done-jobs/$', views.done_jobs, name="done_jobs"),
	url(r'^our_services/web-dev/$', views.web_dev, name="web_dev"),
	url(r'^our_services/blog-dev/$', views.blog_dev, name="blog_dev"),
]



