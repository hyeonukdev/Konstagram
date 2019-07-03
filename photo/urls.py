from django.urls import path
from django.views.generic.detail import DetailView

from .views import *
from .models import Photo

app_name = 'photo'

urlpatterns = [
    path('', photo_list,name='photo_list'),
    path('detail/<int:pk>/',DetailView.as_view(model=Photo,template_name='photo/detail.html'), name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]
<<<<<<< HEAD

# from django.conf.urls.static import static
# from django.conf import settings

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
d
>>>>>>> cfda33dbb70e0c7f55a8039c576d0e370cb2bfe4
