from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Acter(models.Model):
	first_name			=		models.CharField(max_length=64)
	second_name			=		models.CharField(max_length=64)
	biography			=		models.TextField(blank=True, null=True)
	image 				=		models.ImageField(upload_to='acters')

	def __str__(self):
		return '{} {}'.format(self.first_name, self.second_name)


class Movie(models.Model):
	FILE_EXTENTIONS = ['mp4', 'mov',"moov", 'mod']
	preview			=		models.ImageField(upload_to='movie/preview')
	title			=		models.CharField(max_length=64)
	description 	=		models.TextField()

	movie 			=		models.FileField(upload_to='movie/', validators=[FileExtensionValidator(FILE_EXTENTIONS)])

	likes 			=		models.PositiveSmallIntegerField(default=0)
	dislikes		=		models.PositiveSmallIntegerField(default=0)

	acters 			=		models.ManyToManyField(Acter)

	def __str__(self):
		return self.title