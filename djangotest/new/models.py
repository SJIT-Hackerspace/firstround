from django.db import models
from django.contrib.auth.models import User  
  
 
class ScoreBoard(models.Model):


    """Describes the Entrance Scores of Participnats """
    Username = models.ForeignKey(User, on_delete=models.CASCADE,primary_key=True)
    Prob1 = models.IntegerField(default=0)
    Prob2 = models.IntegerField(default=0)
    Prob3 = models.IntegerField(default=0)
    Prob4 = models.IntegerField(default=0)
    Prob5 = models.IntegerField(default=0)
 
    
    def  __str__(self):
        return self.Username + '|' + str(self.Prob1) + '|' + str(self.Prob2) + '|' + str(self.Prob3) + '|' + str(self.Prob4) + '|' + str(self.Prob5)
