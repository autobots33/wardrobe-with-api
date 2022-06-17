from .import views
from django.urls import path,include
from .routers import router
from rest_framework.authtoken import views
#from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
path('user/',views.getUser), 
path('adduser/',views.addUser),
path('user/<int:id>',views.updateUser),
path('user/<int:id>',views.deleteUser),  
path('api/', include(router.urls)),
path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]

#urlpattern= format_suffix_patterns(urlpatterns)