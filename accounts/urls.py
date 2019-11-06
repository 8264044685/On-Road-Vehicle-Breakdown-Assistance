from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('register',views.register,name='register'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('location',views.location_view,name='location'),
    path('booking',views.booking,name='booking'),
    path('load_carModel',views.load_carModel,name='load_carModel'),
    path('load_mechanics',views.load_mechanics,name='load_mechanics'),
    path('search_mechanics', views.search_mechanics, name='search_mechanics'),
    # path('book_mechanics',views.book_mechanics,name='book_mechanics'),
    path('books_mechanics',views.books_mechanics,name='books_mechanics'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('show_request',views.show_request,name='show_request'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('<int:request_accept_id>',views.request_handle,name="request_handle"),
    # path('<int:request_user_id>',views.request_handle_user,name="request_handle_user")

    
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

