from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "DealsHub Admin"
admin.site.site_title = "DealsHub Admin Portal"
admin.site.index_title = "Welcome to DealsHub Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('deals.urls')),
]

from django.views.static import serve
from django.urls import re_path

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
