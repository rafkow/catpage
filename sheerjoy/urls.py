from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'sheerjoy'

urlpatterns = [
    path('', views.index, name="index"),
    path('koty/', views.koty, name="koty"),
    path('gallery/', views.gallery, name="gallery"),
    path('felinoterapia/', views.felinoterapia, name="felinoterapia"),
    path('dyplomy/', views.dyplomy, name="dyplomy"),
    path('pawpeds/', views.pawpeds, name="pawpeds"),
    path('seminaria/', views.seminaria, name="seminaria"),
    path('mioty/',  views.mioty, name="mioty"),
    path('miot/<int:id>', views.miot, name="miot")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
