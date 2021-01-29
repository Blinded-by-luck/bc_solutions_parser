from django.contrib import admin

# Register your models here.
from .forms import BlocksForm
from .models import Blocks

@admin.register(Blocks)
class BlocksAdmin(admin.ModelAdmin):
	list_display = ('id', 'hash', 'height',
				    'timestamp', 'miner', 'transactionCount')
	form = BlocksForm