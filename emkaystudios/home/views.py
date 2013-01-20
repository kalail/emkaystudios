from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Philosophy, Description


def index(request):
	"""
	Homepage with descriptions and information.

	Variables
	-description
	-philosophies

	"""
	# Get variables
	description = Description.objects.all()[0]
	philosophies = Philosophy.objects.filter(order__lte=2).order_by('order')
	return render_to_response(
		'base.html',{
			'description': description,
			'philosophies': philosophies,
		},
		context_instance=RequestContext(request)
		)