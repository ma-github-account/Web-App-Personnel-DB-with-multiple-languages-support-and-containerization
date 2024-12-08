from django.db import models
from django.urls import reverse


class Contact(models.Model):

	fname = models.CharField(max_length=30, db_index=True)
	lname = models.CharField(max_length=30, db_index=True)
	personal_phone = models.CharField(max_length=30, db_index=True)
	work_phone = models.CharField(max_length=30, db_index=True)
	address = models.CharField(max_length=30, db_index=True)

	class Meta:
	
		ordering = ('lname',)
		verbose_name = 'contact'
		verbose_name_plural = 'contacts'
	
	def __str__(self):
	
		return self.lname
	
	def get_absolute_url(self):
	
		return reverse('organizer:contact_detail', args=[self.id])





















































