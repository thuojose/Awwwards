from awewards import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path,include
from django.conf import settings


urlpatterns=[
    path('', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/',views.home, name='home'),
    path('project/<int:project_id>[0-9]',views.project,name ='project'),
     path('profile/',views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)