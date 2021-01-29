from django import forms

from .models import Blocks

class BlocksForm(forms.ModelForm):
	class Meta:
		model = Blocks
		fields = (
				  'id',
				  'hash',
				  'height',
				  'timestamp', 
				  'miner', 
				  'transactionCount'
		)
		widgets = {
			'title': forms.TextInput,
		}