from django.core.management.base import BaseCommand

import requests
from blocks.models import Blocks
import json

class Command(BaseCommand):
	help = 'Импорт bcschain api'
	def handle(self, *args, **options):
		print("::: Очистка базы данных")
		entries= Blocks.objects.all()
		entries.delete()
		print("::: Очистка базы данных завершена")
		print("::: Обновление данных")
		counter = 0
		exec("for i in {}: \n \
		      Blocks(hash = i['hash'], \
				     height = i['height'], \
				     miner = i['miner'], \
			         timestamp = i['timestamp'], \
			         transactionCount = i['transactionCount']).save()".format(requests.get('https://bcschain.info/api/blocks').text))
		print('::: Обновление базы данных завершено')