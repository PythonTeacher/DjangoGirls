# urls.py urlresolver가 사용하는 패턴 목록을 포함하고 있는 파일

"""DjangoGirls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
]

# regex 규칙
# ^ : 문자열 시작
# $ : 문자열 끝
# \d : 숫자
# + : 바로 앞의 항목이 계속 나올 때
# () : 패턴의 부분을 지정할 때
# ex) http://www.mysite.com/post/12345 -> ^post/(\d+)/$