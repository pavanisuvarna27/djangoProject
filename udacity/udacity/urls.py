"""udacity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from courses import views as courses_view
from users import views as users_view
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('udacity/',courses_view.home,name='home'),
    path('udacity/dummy',courses_view.dummydetails,name='dummydetails'),
    path('udacity/adddetails',courses_view.Adddummies,name='Adddummies'),
    path('udacity/names',courses_view.names,name='names'),
    path('udacity/edit/<int:dummy_id>',courses_view.editdetails,name='editdetails'),
    path('udacity/delete/<int:del_id>',courses_view.deletedetails,name='deletedetails'),
    path('register/',users_view.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path("profile/",users_view.profile,name='profile')

]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    