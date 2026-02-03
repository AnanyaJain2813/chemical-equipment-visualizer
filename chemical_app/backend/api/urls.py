from django.urls import path
from .views import UploadCSV, Summary, DownloadReport

urlpatterns = [
    path("upload/", UploadCSV.as_view(), name="upload"),
    path("summary/", Summary.as_view(), name="summary"),
    path("download/", DownloadReport.as_view(), name="download"),
]
