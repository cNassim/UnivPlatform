from django.db import models

class Agent(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    student_id = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name
