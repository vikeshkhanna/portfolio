from django.db import models

def get_artist_pic_folder(instance, filename):
	return "music/artists/" + instance.resolved_name() + "/" + filename

def get_song_folder(instance, filename):	
	return "music/songs/" + instance.artist.resolved_name() + "/" + instance.album.resolved_name() + "/" + filename

def get_album_folder(instance, filename):
	return "music/artists/" + instance.resolve_name() + "/" + filename

class Song(models.Model):
	title = models.CharField(max_length=100)
	lyrics = models.TextField(max_length=2000)
	pid = models.CharField(max_length=100, db_index=True)
	artist = models.ForeignKey('music.Artist')
	album = models.ForeignKey('music.Album', blank=True, null=True)
	genre = models.ForeignKey('music.Genre', blank=True, null=True)

	def __unicode__(self):
		return self.title 

class Artist(models.Model):
	name = models.CharField(max_length=100)
	pid = models.CharField(max_length=100)
	pic_small = models.ImageField(upload_to=get_artist_pic_folder, blank=True, null=True)
	pic_large = models.ImageField(upload_to=get_artist_pic_folder, blank=True, null=True)
	
	def __unicode__(self):
		return self.name

	def resolved_name(self):
		return self.name.replace(" ","_") + "_" + str(self.id)

class Album(models.Model):
	title = models.CharField(max_length=100)
	cover = models.ImageField(upload_to=get_album_folder, blank=True, null=True)
	
	def __unicode__(self):
		return self.title
	
	def resolved_name(self):
		return self.title.replace(" ","_") + "_" + str(self.id)

class Genre(models.Model):
	title = models.CharField(max_length=100)
