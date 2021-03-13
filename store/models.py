from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.tag



#Product
class Tutorial(models.Model):

    DIFFICULTY = (
                ('Beginner', 'Beginner'),
                ('Intermediate', 'Intermediate'),
                ('Advanced', 'Advanced')
    )

    LANGUAGE = (
                ('Korean', 'Korean'),
                ('English', 'English')
    )

    FORMAT = (
                ('Video', 'Video'),
                ('Article', 'Article')
    )

    title                         = models.CharField(max_length=150)
    instructor                    = models.CharField(max_length=150)
    link                          = models.URLField(max_length=2000)
    last_updated                  = models.DateField(max_length=100)
    duration                      = models.CharField(max_length=100) #less than 30/ 30-60/ 60 up
    description                   = models.TextField(max_length=2000)
    thumbnail                     = models.CharField(max_length=500, null=True)
    video                         = models.CharField(max_length=500, null=True)
    language                      = models.CharField(max_length=100, choices=LANGUAGE)
    difficulty                    = models.CharField(max_length=100, choices=DIFFICULTY)
    format                        = models.CharField(max_length=100, choices=FORMAT)
    tags                          = models.ManyToManyField(Tag)

    topic                         = models.CharField(max_length=50)
    digital                       = models.BooleanField(default=False, null=True, blank=False)
    image                         = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.title) + ' | ' + str(self.instructor)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    #curriculum = models.ForeignKey(Curriculum, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

#Order
class Curriculum(models.Model):
    topic                         = models.CharField(max_length=30, null=True)
    date_created                  = models.DateTimeField(auto_now_add=True, null=True)
    goal                          = models.CharField(max_length=150, null=True)
    note                          = models.CharField(max_length=500, null=True, blank=True)

    complete                      = models.BooleanField(default=False)
    curriculum_id                 = models.CharField(max_length=150, null=True)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.topic)


#OrderItem
class CurriculumItem(models.Model):
    tutorial                      = models.ForeignKey(Tutorial, null=True, on_delete=models.SET_NULL)
    curriculum                    = models.ForeignKey(Curriculum, null=True, on_delete=models.SET_NULL)


