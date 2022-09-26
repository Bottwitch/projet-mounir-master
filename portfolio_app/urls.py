from django.urls import path
from .views import protfolio


urlpatterns = [
	path("portfolio/", protfolio)

]


