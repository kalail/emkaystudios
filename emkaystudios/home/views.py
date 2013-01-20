from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Philosophy, Description, TechnicalSkill
from blog.models import Post


def index(request):
	"""
	Homepage with descriptions and information.

	Variables
	-description
	-philosophies
	-technical_skills
	-blog_posts

	"""
	# Get variables
	description = Description.objects.all()[0]
	philosophies = Philosophy.objects.filter(order__lte=2).order_by('order')
	technical_skills = TechnicalSkill.objects.filter(order__lte=2).order_by('order')
	blog_posts = Post.objects.all().order_by('-created_on')[0:4]
	
	return render_to_response('base.html',
		{
			'description': description,
			'philosophies': philosophies,
			'technical_skills': technical_skills,
			'blog_posts': blog_posts,
		},
		context_instance=RequestContext(request))