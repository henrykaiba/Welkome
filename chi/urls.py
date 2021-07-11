from django.urls import path
from .views import index, faq, useful, contact, search, detail_faq, detail_useful


app_name = "chi"
urlpatterns = [
    path('index_c/', index, name="index"),
    path('faq/', faq, name="faq"),
    path('useful/', useful, name="useful"),
    path('contact/', contact, name="contact"),
    path('search/', search, name="search"),
    path('detail_faq/<int:post_id>/', detail_faq, name="detail_faq"),
    path('detail_useful/<int:post_id>/', detail_useful, name="detail_useful"),
]
