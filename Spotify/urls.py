from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mainApp.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("albomlar", AlbomlarModelViewSet),
router.register("qushiqchilar", QoshiqchilarModelViewSet),
router.register("qushiqlar", QoshiqModelViewSet),
urlpatterns = ([
                  path('admin/', admin.site.urls),
                  path('', include(router.urls)),
                  path('qoshiqlar/', QoshiqAPI.as_view()),
                  path('qoshiqchilar/', QoshiqchilarAPI.as_view()),
                  path('qoshiqchi/<int:pk>/', QoshiqchiAPI.as_view()),
                  path('del_qoshiqchi/<int:pk>/', QoshiqchiAPI.as_view()),
                  path('upd_qoshiqchi/<int:pk>/', QoshiqchiAPI.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
