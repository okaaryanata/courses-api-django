from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Courses(models.Model):
    # karena setelah migrate nama table menjadi courses_courses, dan kita ingin mmengganti
    # maka harus tambahkan meta
    class Meta:
        db_table = "courses"

    # main feilds
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.TextField(blank=True, default="")
    video_url = models.CharField(max_length=128)
    price = models.FloatField(default=0)
    image_url = models.CharField(max_length=128, null=True, blank=True)

    # Relations
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    
    def __str__(self):
        return self.title