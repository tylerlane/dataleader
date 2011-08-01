from django.db import models
from django.contrib.localflavor.us.us_states import STATE_CHOICES

FEEDBACK_TYPE_CHOICES = (
    ('letter_to_editor','Letter To The Editor'),
    ('voice_of_day','Voice of the Day'),
    ('to_the_point','To The Point'),
    ('rose_thorn', 'Roses and Thorns'),
    ('feedback','Story Feedback'),
    ('story_idea','Story Idea'),
    ('press_release','Press Release' ),
    ('you_asked', 'You Asked' ),
    ('other','Other' )
    )
COPPA_CHOICES = (
    ('under13','12 or under'),
    ('13-17','13 - 17'),
    ('18-20','18 - 20'),
    ('21-24','21 - 24'),
    ('25-34','25 - 34'),
    ('35-49','35 - 49'),
    ('50-64','50 - 64'),
    ('over65','65 or over'),
    )
# Create your models here.
class Feedback(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=15,choices=STATE_CHOICES)
  phone = models.CharField(max_length=25)
  email = models.CharField(max_length=255)
  message = models.TextField(blank=False,null=False,default="message goes here")
  feedback_type = models.CharField(max_length=50,choices=FEEDBACK_TYPE_CHOICES)
  time_init = models.DateTimeField( "Date Added", auto_now = False, auto_now_add = True, null=False, blank = False )
  coppa = models.CharField( max_length=15, choices=COPPA_CHOICES)
  objects = models.Manager()

  def __unicode__( self ):
    return self.feedback_type + ": " + self.name 

  class Meta:
    verbose_name = "Feedback"
    verbose_name_plural = "Feedback items"
