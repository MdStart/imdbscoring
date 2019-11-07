"""imdbscoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from score.views import (
	ImdbScoreCreateAPIView,
	ImdbScoreDataAPIView,
	ImdbScoreUpdateAPIView,
	ImdbScoreDeleteAPIView,
	ImdbScoreSearchAPIView,

	)

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Welcome to Imdb Scoring API')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^imdb-score/create', ImdbScoreCreateAPIView.as_view(), name='create'),
    url(r'^imdb-scores/list', ImdbScoreDataAPIView.as_view(), name='list_view'),
    url(r'^imdb-score/(?P<id>\d+)/edit', ImdbScoreUpdateAPIView.as_view(), name='edit'),
    url(r'^imdb-scores/search', ImdbScoreSearchAPIView.as_view(), name='search'),
    url(r'^imdb-score/(?P<id>\d+)/delete', ImdbScoreDeleteAPIView.as_view(), name='delete'),
    url(r'^|imdb-scores/doc', schema_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)