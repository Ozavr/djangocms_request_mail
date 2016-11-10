from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from tagilturist import settings

# Our model
from request_mail.models import RequestList

class CreateRequest( SuccessMessageMixin, CreateView ):
	'''
	Controller for recording information of client in list of request and sending 
	request for the managers
	Контроллер для создание записи клиента в базе данных и отправки запроса менджерам
	'''
	model = RequestList
	template_name = 'request.html'
	fields = [ 'name', 'phone_number', 'description' ]
	success_message = 'Спасибо за вашу заявку, наши менеджеры свяжутся с вами в ближайшое время!'
	success_url = 'news'

	def form_valid( self, form ):
		'''
		sending email request
		'''
		output = super( CreateRequest, self ).form_valid( form )
		request_message = 'Запрос клиента с сайта tagilturist.ru!\n\n' +
			'Имя: ' + form.instance.name + '\n' +
			'Телефон: ' + form.instance.phone + '\n' +
			'Краткая информация запроса: ' +  form.instance.description

		send_mail( 'Запрос клиента', request_message, fail_silently = True )
		return output