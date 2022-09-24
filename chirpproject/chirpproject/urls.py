from django.contrib import admin
from django.urls import path, include

# Since our homepage is located in the chirpapp, we need make our route to the chirpapp '' so we can load the homepage when the app is launched (in chirpapp.urls.py, you'll also need to point the index route to '' for this to work). Otherwise, we'll get a 'page not found' error that requires us to enter the route by hand. 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chirpapp.urls')),
    path('users/', include('users.urls'))
]


