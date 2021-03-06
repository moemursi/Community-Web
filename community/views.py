import feedparser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .communities.models import Community, CommunityUserProfile
from .meetups.models import Meetup, Attendee
from .notifications.models import Notification
from django.db.models import Q



def home(request):
    if request.user.is_authenticated:
        return home_login(request)
    else:
        context = {

        }
        return render(request, template_name='index_1.html')#context=context)


@login_required
def home_login(request):
    user = request.user
    all_communities = Community.objects.all()
    my_communities = Community.objects.filter(communityuserprofile__in=CommunityUserProfile.objects.filter(user=user, active=True))
    user_attending = Attendee.objects.exclude(status=Attendee.STATUS_CHOICES[2][0]).filter(user=user)
    meetup_list = Meetup.objects.filter(Q(attendee__in=user_attending) & Q(active=True))
    notifications = Notification.objects.filter(user=user).order_by('-date')[:2]
    feed = feedparser.parse('https://www.uwb.edu/news?rss=blogs')
    entries = feed.entries
    num_entries = 5
    context = {
        'user': request.user,
        'all_communities': all_communities,
        'my_communities': my_communities,
        'community': all_communities.first(),
        'meetup_list': meetup_list,
        'notifications_list': notifications,
        'feed': feed,
        'entries': entries,
        'num_entries': num_entries,
    }
    return render(request, template_name='dashboard.html', context=context)
