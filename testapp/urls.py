from django.urls import path
import testapp.views as testapp_views

urlpatterns = [
    path("", testapp_views.product_list, name="product_list"),
    path("<int:product_id>/", testapp_views.get_product_by_id, name="product_info")
]