from django.db import models
class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    age = models.IntegerField(null=True)
    friends=models.ManyToManyField('self', through='FriendShip',
                                      symmetrical=False)

    def __str__(self):
        return self.name

class FriendShip(models.Model) :
    from_student = models.ForeignKey('Student',related_name='from_student',on_delete=models.CASCADE)
    to_student = models.ForeignKey('Student',related_name='to_student',on_delete=models.CASCADE)
    class Meta:
        unique_together = ('from_student', 'to_student')