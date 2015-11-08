from django.conf.urls import url
from . import views

urlpatterns = [
    # name은 URL에 이름을 붙여 view를 식별하는데 사용
    url(r'^$', views.post_list, name='post_list'),  # http://127.0.0.1:8000
    # <pk> : 여기에 넣은 모든 것을 pk 변수에 넣어 뷰로 전송하겠다는 뜻입니다
    # http://127.0.0.1:8000/post/5/입력하면, 장고는 post_detail인 view를 찾고 있다고
    # 생각하고 pk가 5와 일치한 view 로 정보를 보내게 됩니다..
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),  # http://127.0.0.1:8000/post/1/
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]