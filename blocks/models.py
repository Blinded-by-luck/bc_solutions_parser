from django.db import models

# Create your models here.
class Blocks(models.Model):
	id = models.BigIntegerField(primary_key=True) # id primary key
	hash = models.CharField(max_length=100) # хэш блока
	height = models.BigIntegerField() # высота блока
	timestamp = models.BigIntegerField() # время блока
	miner = models.CharField(max_length=100) # адрес майнера
	transactionCount = models.BigIntegerField() # кол-во транзакций в блоке
	
	class Meta:
		verbose_name = 'Блок'
		verbose_name_plural = 'Блоки'
		ordering = ['id']