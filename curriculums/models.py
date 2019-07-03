from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curriculums(models.Model):
    # karena setelah migrate nama table menjadi curriculums_curriculums, dan kita ingin mmengganti
    # maka harus tambahkan meta
    class Meta:
        db_table = "curriculums"

    # main feilds
    title = models.CharField(max_length=128)
    attachment_url = models.CharField(max_length=128)
    type = models.CharField(max_length=64)
    # Relations
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    course = models.ForeignKey('courses.Courses', on_delete=models.CASCADE, null=True,related_name='curriculums')

    
    def __str__(self):
        return self.title