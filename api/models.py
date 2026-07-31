from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self) -> str:
        return str(self.title)

class Project(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    impact = models.TextField()
    
    def __str__(self) -> str:
        return str(self.name)

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    scope = models.TextField()
    budget_range = models.CharField(max_length=100)
    timeline = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.name)