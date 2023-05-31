from django.urls import path

from webapp.views.cat_stats import add_view
from webapp.views.base import index_view

urlpatterns = [
    path('', index_view),
    path('cat_stats/', add_view)
]
