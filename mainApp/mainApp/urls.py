from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('test.urls')),
    path('api/v1/', include('question.urls')),
    path('api/v1/', include('testresult.urls')),
    path('api/v1/', include('answer.urls')),
]
