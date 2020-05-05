from django.db import models

# Create your models here.
class TimeStampModel(models.Model):

    """ TIme Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        """ 
        데이터베이스에 표시되지 않게 하기 위해 abstract 를 사용함
        추상적 데이터 베이스로 아래 변수를 선언하지 않으면 데이터베이스에 등록됨
        """

        abstract = True
