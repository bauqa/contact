from django.urls import path,include
from . import views
urlpatterns = [
    path('feed/',views.Index.as_view(),name="index"),
    path('',views.quest,name="what"),
    path('accounts/',include('django.contrib.auth.urls')),
    
    path('reg/',views.signup,name="registration"),
    path('profile/<int:pk>/',views.Profile.as_view(),name="profile"),
    path('post/<int:pk>',views.PostView.as_view(),name="postUrl"),
    path('profile/<int:pk>/edit/',views.ProfileEdit.as_view(),name="profileEdit"),
    path('postadd/',views.postadd,name="postadd"),
    path('comment/add/<int:id>/',views.commentadd,name="commentadd"),
    path('comment/parent/add/<int:id>/',views.parent_comment,name="parent_comment")
    
]