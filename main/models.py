from django.db import models
#from django.contrib.auth.models import User
#from thumbs import ImageWithThumbsField

# Create your models here.

class User(models.Model):
    #user = models.CharField(max_length = 50)
    nick_name = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    image_owner = models.ImageField (upload_to = 'photo',blank = True, null = True)
    password = models.CharField(max_length = 50)
    birth_date = models.DateField()
    email = models.CharField(max_length = 50)
    place = models.CharField(max_length = 50)
    biography = models.CharField(max_length = 50)
    place_birth = models.CharField(max_length = 50)
    follow = models.ManyToManyField('self', related_name='following', blank=True)
   
    def __unicode__(self):
        return 'User: %s - %s %s' % (self.pk, self.last_name, self.first_name) 
   
#def get_profile(user):
#	if not hasattr(user, '_profile_cache'):
 #       	profile, created = Perfil.objects.get_or_create(user=user)
  #      	user._profile_cache = profile
   # 	return user._profile_cache

#User.get_profile = get_profile



class Tweet(models.Model):
    owner = models.ForeignKey('User', related_name='tweets')
    status = models.CharField(max_length = 50 )
    created_at = models.DateTimeField(auto_now_add=True)
