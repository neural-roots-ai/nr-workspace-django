from django.contrib import admin
from django.urls import path
from client.views import login


admin.site.site_title = "Neural Roots Site admin"
admin.site.site_header = "Neural Roots administration"
admin.site.index_title = "Neural Roots administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, basename='login'),
]
