from django.db import models

# Create your models here.

class Player(models.Model):
    first=models.CharField(max_length=15)
    last=models.CharField(max_length=20)
    position=models.CharField(max_length=20, null=True)

    
   
    technique=models.IntegerField( null=True)
    mindset=models.IntegerField( null=True)
    gameIntelligence=models.IntegerField(null=True)
    teamPlayer=models.IntegerField( null=True)
    endurance=models.IntegerField( null=True)

    strength=models.IntegerField( null=True)
    speed=models.IntegerField( null=True)
    skill_level=models.IntegerField( null=True)
    def __str__(self):
        return f"{self.id} {self.first} {self.last} : {self.skill} {self.strength} {self.speed}"
    

  