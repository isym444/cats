from django.db import models



class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    number_of_cats = models.IntegerField(default=0)

    def __str__(self):
        return self.firstname


class Cat(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='cats')

    def __str__(self):
        return self.cat_name

    class Meta:
        ordering = ['cat_name']  # Orders Cats by cat_name in ascending order
