from django.urls import path

from reference import views

urlpatterns = [
    path("", views.ReferenceRequestView.as_view(), name="refer-request"),
    path("comment", views.ReferenceView.as_view(), name="refer-comment"),
]
