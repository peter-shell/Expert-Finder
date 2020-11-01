from django.urls import path
from . import views

app_name = "expertFinder"

urlpatterns = [
    path("", views.index, name="editUserForm"),
    path("<int:pk>/", views.display_expert, name="display_expert"),
    path("search_results", views.search_results, name='search_results'),
]
handler400 = 'expertFinder.error_handlers.bad_request'
