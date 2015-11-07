from django.conf.urls import url
from . import views

urlpatterns = [
    # name은 URL에 이름을 붙여 view를 식별하는데 사용
    url(r'^$', views.post_list, name='post_list'),  # http://127.0.0.1:8000
]