from django.db import models

class Experiment(models.Model):
    name        = models.CharField(max_length=100)

class Subject(models.Model):
    name        = models.CharField(blank=True, max_length=100)
    subject_id  = models.CharField(blank=True, max_length=100)
    experiment  = models.ForeignKey(Experiment)
    path        = models.FilePathField(path="/Users/pealco/archive/data")

class Epoch(models.Model):
    trigger     = models.IntegerField()
    condition   = models.CharField(max_length=100)
    word_num    = models.PositiveIntegerField()
    subject     = models.ForeignKey(Subject)

class Measurement(models.Model):
    value       = models.DecimalField(max_digits=10, decimal_places=10)
    index       = models.IntegerField()
    subject     = models.ForeignKey(Subject)
    experiment  = models.ForeignKey(Experiment)
    electrode   = models.CharField(max_length=4)
