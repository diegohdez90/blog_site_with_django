from django.conf.urls import url
from blog import views

urlpatterns = [
  url(r'^$', views.PostListView.as_view(), name='post_list'),
  url(r'^(?P<pk>\d+)/post/$', views.PostDetailView.as_view(), name='post_detail'),
  url(r'^post/new/$',views.CreatePostView.as_view(), name='post_new'),
  url(r'^(?P<pk>\d+)/post/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
  url(r'^(?P<pk>\d+)/post/delete/$', views.PostDeleteView.as_view(), name='post_delete'),
  url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
  url(r'^about/$', views.AboutView.as_view(), name='about'),
]
