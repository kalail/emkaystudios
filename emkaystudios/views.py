from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from emkaystudios.models import Announcement
from blog.models import Post
from itertools import chain
from operator import attrgetter
from emkaystudios.settings import TWITTER_USERNAME
import twitter

def index(request):
	try:
		latest_announcement = Announcement.objects.latest('created_on')
	except Announcement.DoesNotExist:
		return HttpResponseRedirect(reverse('emkaystudios.views.about'))

	latest_announcements = Announcement.objects.all().order_by('-created_on')[1:4]
	latest_blog_posts = Post.objects.all().order_by('-created_on')[:3]
	latest_tweets = twitter.Api().GetUserTimeline(TWITTER_USERNAME)[:5]

	latest_items = sorted(
		chain(latest_announcements, latest_blog_posts),
		key=attrgetter('created_on')
		)
	latest_items.reverse()
	latest_items = latest_items[:3]

	return render_to_response('index.html', {'latest_announcement': latest_announcement, 'latest_items': latest_items, 'latest_tweets': latest_tweets }, context_instance=RequestContext(request))


def about(request):
	return render_to_response('about.html', context_instance=RequestContext(request))

def contact(request):
	return HttpResponseRedirect(reverse('emkaystudios.views.coming_soon'))

def archive(request):
	return HttpResponseRedirect(reverse('emkaystudios.views.coming_soon'))

def coming_soon(request):
	return render_to_response('coming_soon.html', context_instance=RequestContext(request))