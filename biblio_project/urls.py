"""biblio_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from biblio_app.views import MainCategoryView, SubCategoryView, CertainSubCategoryView, FormsView

urlpatterns = [
    path('admin/', admin.site.urls),
    url('main-category/$', MainCategoryView.as_view(), name='main-category'),
    url('main-category/(?P<category_id>(\d)+)$', SubCategoryView.as_view(), name='subcategory'),
    url('^main-category/(?P<category_id>(\d)+)/(?P<subcategory_id>(\d)+)$', FormsView.as_view(), name="certain-subcategory")
]
