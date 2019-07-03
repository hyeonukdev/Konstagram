from django.urls import path
from django.contrib.auth import views as auth_view

from .views import register

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),
]
<<<<<<< HEAD

# from django.conf.urls.static import static
# from django.conf import settings

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
>>>>>>> cfda33dbb70e0c7f55a8039c576d0e370cb2bfe4
