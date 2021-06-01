from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    id = models.IntegerField(primary_key = True)
    employee_name = models.CharField(max_length=80)
    employee_email = models.EmailField()
    employee_age = models.IntegerField()
 
    def __str__(self):
        return f"{self.employee_name} : {self.employee_age}"
