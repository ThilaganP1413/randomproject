from django.db import models

class Student(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    fullname = models.CharField(max_length=200, null=True)
    regno = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    balance = models.DecimalField(decimal_places=2,max_digits=7,default=0.0)


    def __str__(self):
        return self.fullname
