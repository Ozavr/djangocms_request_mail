from django.conf.urls import url

#Our controllers
from request_mail.views import CreateRequest, SuccessMessage

urlpatterns = [
	url( r'^$', CreateRequest.as_view(), name = 'request' ),
	url( r'^success/$', SuccessMessage.as_view(), name = 'request_success' ),
]