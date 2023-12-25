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

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Spotify loyihasi uchun Doc fayl',
        default_version='v1.0',
        description='Front-end, Android, Desktop dasturchilar uchun Blog-API DOCS',
        contact=openapi.Contact(email='AkmaljonGold@gmail.com'),
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticatedOrReadOnly],
)

urlpatterns = ([
                   path('swagger_doc_of_spotify/', schema_view.with_ui('swagger', cache_timeout=0)),
                   path('admin/', admin.site.urls),
                   path('', include(router.urls)),
                   path('qoshiqlar/', QoshiqAPI.as_view()),
                   path('qoshiqchilar/', QoshiqchilarAPI.as_view()),
                   path('qoshiqchi/<int:pk>/', QoshiqchiAPI.as_view()),
                   path('del_qoshiqchi/<int:pk>/', QoshiqchiAPI.as_view()),
                   path('upd_qoshiqchi/<int:pk>/', QoshiqchiAPI.as_view()),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
