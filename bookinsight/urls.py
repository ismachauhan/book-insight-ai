from django.contrib import admin
from django.urls import path, include
from library.views import dashboard, ask_page, book_detail, history_page

urlpatterns = [
    path('', dashboard),
    path('ask/', ask_page),
    path('book/<int:pk>/', book_detail),

    path('history/', history_page), 

    path('admin/', admin.site.urls),
    path('api/', include('library.urls')),  # API routes
]