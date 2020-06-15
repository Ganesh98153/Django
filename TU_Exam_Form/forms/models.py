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


    SEM_LISTS = [

    ("1st", "1st"),
    ("2nd", "2nd"),
    ("3rd", "3rd"),
    ("4th", "4th"),
    ("5th", "5th"),
    ("6th", "6th"),
    ("7th", "7th"),
    ("8th", "8th"),
    ]
    TYPE_LISTS = [

        ("Compulsory", "Compulsory"),
        ("Elective", "Elective"),
    ]

    subject_name = models.CharField(max_length=30)
    subject_code = models.CharField(max_length=7)
    subject_semester = models.CharField(max_length =7, choices=SEM_LISTS)
    subject_type = models.CharField(max_length=12, default="Compulsory", choices=TYPE_LISTS)

    def __str__(self):
        return self.subject_name
