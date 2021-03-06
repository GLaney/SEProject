"""seproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include

from app.views import *
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('health/', health),
    path('contact/', contact),
    path('operation/', operation, name='operation'),
    path('policies/', policies),
    path('technologies/', technologies),
    path('faq/', faq),
    path('register/', register),
    path('login/', loginPage),
    path('accounts/', include('django.contrib.auth.urls')),
    path('operation/budgets/', RedirectView.as_view(url='https://bursar.columbusstate.edu/fees.php')),
    path('operation/campu/', RedirectView.as_view(url='https://students.columbusstate.edu/campus-life.php')),
    path('operation/orient/', RedirectView.as_view(url='https://orientation.columbusstate.edu')),
    path('operation/calendar/', RedirectView.as_view(url='https://academics.columbusstate.edu/calendars/')),
    path('operation/dining/', RedirectView.as_view(url='https://columbusstate.campusdish.com')),
    path('operation/rec/', RedirectView.as_view(url='https://campusrec.columbusstate.edu')),
    path('screener/', screener),

    ######################## Forum #################################
    path('forumMain/',forumMain,name='forumMain'),
    path('forumHome/',forumHome,name='forumHome'),
    #path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
    path('forumMain/<forumName>/',forumView,name='forumView'),
    path('forumMain/<forumName>/addInForum/',addInForum,name='addInForum'),
    path('forumMain/<forumName>/<forumTopic>/', forumDiscussion, name='forumDiscussion'),
    path('like/<forumTopic>', LikeView, name='like_post'),
    path('userDiscussions/', userDiscussions, name='userDiscussions'),
    path('forumMain/search/<searchTerm>/', searchView, name='search')
    
     ####################### Forum ################################
]
