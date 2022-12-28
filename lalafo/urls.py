from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.settings.views import index
from apps.products.views import product_detail,product_create,product_search, product_index
from apps.users.views import register,user_login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('product/<int:id>/',product_detail, name ="product_detail"),
    path('register/', register, name = "register"),
    path('logout/', LogoutView.as_view(next_page = "index"), name = "logout"),
    path('login/', user_login, name = "user_login"),
    path('product/create/',product_create, name = "product_create"),
    path('product/search/',product_search,name='product_search'),
    path('product_index/', product_index, name = "product_index")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)