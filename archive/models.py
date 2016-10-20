from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Panel(models.Model):
    origPanelId = models.IntegerField(blank=True)
    origTitle = models.CharField(max_length=64, blank=True)
    BOOKS = (
        ('Gene', 'Genesis'),
        ('Exod', 'Exodus'),
        ('Levi', 'Leviticus'),
        ('Nums','Numbers'),
        ('Deut','Deuteronomy')
        )
    book = models.CharField(max_length=4, choices=BOOKS)
    chapterStart = models.IntegerField()
    verseStart = models.IntegerField()
    chapterEnd = models.IntegerField()
    verseEnd = models.IntegerField()
    title = models.CharField(max_length=32)
    
    def __str__(self):
        return self.title
    
class Participant(models.Model):
    lastName = models.CharField(max_length=35)
    firstName = models.CharField(max_length=35)
    participantType = models.CharField(max_length=30,default="none")
    
    def __str__(self):
        return self.firstName + ' ' + self.lastName
    
class PanelStitchingRecord(models.Model):
    panel = models.ForeignKey(Panel)
    assignedDate = models.DateField()
    receivedDate = models.DateField()
    stitcher = models.ForeignKey(Participant)

    def __str__(self):
        return self.panel.title
    
class UploadData(models.Model):
    datafile = models.FileField(upload_to='imports')

class ImportData(models.Model):
    importDate = models.DateTimeField()