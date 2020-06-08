from django.db import models


class student_info(models.Model):
    year = models.IntegerField(max_length=4)
    faculty = models.CharField(max_length=100)
    batch = models.IntegerField(max_length = 4)
    college = models.CharField(max_length=100)
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    gender = models.CharField(max_length=6)
    phone = models.CharField(max_length=10, default='98--------')
    tu_registraion_number = models.CharField(max_length=15)
    semester = models.CharField(max_length = 5)


    def __str__(self):
        return self.tu_registraion_number



class subjects(models.Model):

    subject_name = models.CharField(max_length=30)
    subject_code = models.CharField(max_length=5)
    sub_semester = models.CharField(max_length =3)

    def __str__(self):
        return self.subject_name
