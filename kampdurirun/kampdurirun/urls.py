"""
URL configuration for kampdurirun project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# from id_card.views import ()
from lampiran.views import (
    custom_access_denied_page,
    download_page,
)

from postingan.views import (
    postingan_list,
    create_postingan,
    my_post,
)

from profil.views import (
    edit_profil,
    create_profil,
)

from user.views import (
    registration_view,
    login_view,
    logout_view,
    home_view,
    change_password_view,
    show_kebijakan_privasi,
)

urlpatterns = [
    # untuk admin
    path("admin/", admin.site.urls),
    
    # user
    path("", home_view, name="home"),
    path("register/", registration_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("login/", login_view, name="login"),
    path('change_password/', change_password_view, name='change_password'),
    path('kebijakan_privasi/', show_kebijakan_privasi, name='kebijakan_privasi'),

    # profil
    path('edit_profil/', edit_profil, name='edit_profil'),
    path('profile/', create_profil, name='create_profil'),

    # postingan
    path("all_posts/", postingan_list, name="all_posts"),
    path("my_posts/", my_post, name="my_posts"),
    path("make_posts/", create_postingan, name="make_posts"),

    # lampiran
    path("access_denied/", custom_access_denied_page, name="custom_access_denied_page"),
    path('download_page/<int:id_dokumen>/', download_page, name='download_page'),
]

# Add this code at the end of your urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)