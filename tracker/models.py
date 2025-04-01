from django.db import models

class Job(models.Model):
    STAGE_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
    ]

    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role} at {self.company}"
