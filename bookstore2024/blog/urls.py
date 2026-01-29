from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.post_list, name='post_list'),
    path('book/<int:pk>/' , views.post_detail, name='post_detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)