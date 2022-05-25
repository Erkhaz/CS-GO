from django.db import models

class csgo(models.Model):
        csgo = models.CharField(max_length=20)
        description = models.CharField(max_length=20)
        birth_date = models.DateField()

        def __str__(self):
            return self.csgo + ' ' + self.description+" " + self.birth_date

class csgoteam(models.Model):
        name = models.CharField(max_length=100)
        teamValue = models.IntegerField(default=1)
        sporttype = models.ManyToManyField(to=csgo)

        def __str__(self):
            return self.name

class csgoplayer(models.Model):
        first_name = models.CharField(max_length=100, null=True)
        last_name = models.CharField(max_length=120, null=True)
        teamname = models.ManyToManyField(to=csgo)
        team = models.ForeignKey(to=csgoteam, null=True, on_delete=models.SET_NULL)

        def __str__(self):
            return self.first_name + ' ' + self.last_name+" " + self.teamname+" "+self.team

