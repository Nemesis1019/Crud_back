from django.urls import path,include
from rest_framework import routers
from Project.views import ProjectView
from rest_framework.documentation import include_docs_urls

router=routers.DefaultRouter()
router.register(r'client',ProjectView,'client')

urlpatterns = [
    path("",include(router.urls)),
    path("docs/",include_docs_urls(title="Projects API"))
]
