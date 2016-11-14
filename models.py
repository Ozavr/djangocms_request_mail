from django.db import models

class RequestList( models.Model ):
	'''
	Model of the list clients request 
	Модель базы данных для базы данных в которую записываются данные клиента при запросе
	'''
	name = models.CharField( max_length = 20, verbose_name = 'Имя' )
	phone = models.CharField( max_length = 20, verbose_name = 'Номер телефона' )
	description = models.TextField( max_length = 350, verbose_name = 'Содержание запроса' )
	date = models.DateTimeField( auto_now_add = True, db_index =True )

	class Meta:
		'''
		Settings for the model
		'''
		ordering = [ '-date' ]
		verbose_name = 'Список запросов'