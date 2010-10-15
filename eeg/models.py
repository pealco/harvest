from django.db import models

class Experiment(models.Model):
    name = models.CharField(max_length=100)

class Subject(models.Model):
    name       = models.CharField(blank=True, max_length=100)
    subject_id = models.CharField(blank=True, max_length=100)
    experiment = models.ForeignKey(Experiment)

class Epoch(models.Model):
    trigger         = models.IntegerField()
    pre_trigger     = models.IntegerField()
    post_trigger    = models.IntegerField()
    electrode       = models.CharField(max_length=4)
    condition       = models.CharField(max_length=100)
    word_num        = models.PositiveIntegerField()
    subject         = models.ForeignKey(Subject)

class Measurement(models.Model):
    value   = models.DecimalField(max_digits=10, decimal_places=10)
    index   = models.IntegerField()
    epoch   = models.ForeignKey(Epoch)