from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
                  # CKEDITOR UPLOADER URL
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('',index,name="index"),
    path('post/',post,name='post'),
    path('login/',LOGIN,name='login'),
    path('doLogin/',doLogin,name='doLogin'),
    path('logout/',llogout,name='logout'),
    path('delete/<int:id>/',delete,name="delete"),
    path('delete_cont/<int:id>/',delete_cont,name="delete_cont"),
    path('qr_code/',qr_all,name="qr_all")
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
