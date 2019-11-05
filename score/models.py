from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator

GENRE_CHOICES = (('Adventure', 'Adventure'), ('Family', 'Family'), ('Fantasy', 'Fantasy'),
					('Musical', 'Musical'), ('Sci-Fi', 'Sci-Fi'), ('Drama', 'Drama'), ('War', 'War'),
						('Romance', 'Romance'), ('Comedy', 'Comedy'), ('Thriller', 'Thriller'),
							('Crime', 'Crime'), ('Horror', 'Horror'), ('History', 'History'), ('Family', 'Family'),
								('Animation', 'Animation'), ('Short', 'Short'), ('Western', 'Western'),
									('Action', 'Action'), ('Biography', 'Biography'))

class ImdbScore(models.Model):
	
	popularity99 = models.FloatField(
		default=0.0,
		validators=[MinValueValidator(0.0), MaxValueValidator(100.0)]
	)
	director = models.CharField(max_length=500, blank=False)
	genres = MultiSelectField(choices=GENRE_CHOICES)
	imdb_score = models.FloatField(
		default=0.0,
		validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
	)
	name = models.CharField(max_length=500, blank=False, unique=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-created',]
