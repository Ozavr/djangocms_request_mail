from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import mail_managers
from django.contrib.messages.views import SuccessMessageMixin
from tagilturist import settings

# Our model
from request_mail.models import RequestList

class CreateRequest( CreateView ):
	'''
	Controller for recording information of client in list of request and sending 
	request for the managers
	Контроллер для создание записи клиента в базе данных и отправки запроса менджерам
	'''
	model = RequestList
	template_name = 'request.html'
	fields = [ 'name', 'phone', 'description' ]
	# success_message = 'Спасибо за вашу заявку, наши менеджеры свяжутся с вами в ближайшое время!'
	success_url = reverse_lazy( 'request_success' )
	def form_valid( self, form ):
		'''
		sending email request
		'''
		output = super( CreateRequest, self ).form_valid( form )

		request_message = 'Запрос клиента с сайта tagilturist.ru!\n\n' 
		request_message += 'Имя: ' + form.instance.name + '\n'
		request_message += 'Телефон: ' + form.instance.phone + '\n' 
		request_message += 'Краткая информация запроса: ' +  form.instance.description

		mail_managers( 'Запрос клиента', request_message )
		return output

class SuccessMessage( TemplateView ):
	'''
	Our success message
	'''
	template_name = 'request_success.html'

