from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from easy_thumbnails.fields import ThumbnailerImageField
import os


def get_profile_image_path(instance, filename):
    return os.path.join('accounts', str(instance.profile.user.id), 'profile', filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.CharField(max_length=60, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    image = models.OneToOneField('ProfileImage', related_name='profile_image', null=True, blank=True)

    def __str__(self):
        return self.user.username + "'s profile"

    class Meta:
        unique_together = ('user', 'id')

class ProfileImage(models.Model):
    image = ThumbnailerImageField(null=False, upload_to=get_profile_image_path)
    profile = models.ForeignKey(Profile, related_name='profile_image', on_delete=models.CASCADE)

    def __str__(self):
        return "{}'s profile pic: {}".format(self.profile.user.username, self.image.name)

    class Meta:
        unique_together = ('profile', 'id')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
