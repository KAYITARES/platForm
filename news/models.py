from django.db import models

class Language(models.Model):
  name=models.CharField(max_length=30)
  def __str__(self):
    return self.name
  class Meta:
    ordering=['name']
class LanguageDetails(models.Model):
  name=models.ForeignKey(Language,on_delete=models.CASCADE)
  table_content=models.CharField(max_length=30)
  title=models.CharField(max_length=80)
  content=models.TextField()
  @classmethod
  def disp(cls):
    nam=LanguageDetails.objects.all()
    return nam