from django.contrib import admin
from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('program',views.program,name = 'program'),
    path('bstudy',views.bstudy,name = 'bstudy'),
    path('fgroup',views.fgroup,name = 'fgroup'),
    path('blog', views.all_post, name="blog"),
    path('post/<int:id>/', views.post_detail, name='blog_detail'),
    path('gallery', views.gallery, name='gallery'),
    path(r'search/', views.search_results, name='search_results'), 
    path('video',views.video,name = 'video'),
    path('contact/', views.contact, name='contact')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)