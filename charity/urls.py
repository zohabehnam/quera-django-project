from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('charities.urls')),
    path('accounts/', include('accounts.urls')),
    path('about-us/', include('about_us.urls')),
]
