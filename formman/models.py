from django.db import models

# Create your models here.
class TestMaster(models.Model):
    test_pk = models.AutoField('プライマリキー',primary_key = True)
    id = models.IntegerField('ID', unique=True)
    name = models.CharField('名', max_length=100)
    number = models.IntegerField('値', blank=False, null=False)

    def __str__(self):
        return self.name
