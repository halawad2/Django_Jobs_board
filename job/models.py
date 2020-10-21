from django.db import models

# Create your models here.
JOB_TYPE = (
    ('Full T ime' , 'Full Time'),
    ('Part Time' , 'Part Time'),
)
class job(models.Model):
    title = models.CharField(max_length=100)
    # location =
    jop_type = models.CharField(max_length=15, choices=JOB_TYPE)
    describtion = models.TextField(max_length=1000 , default='')
    publish_dt = models.DateTimeField(auto_now=False, auto_now_add=False)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    

        