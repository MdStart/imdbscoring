from rest_framework import serializers, fields, validators

from score.models import ImdbScore, GENRE_CHOICES

class ImdbScoreSerializer(serializers.ModelSerializer):
	"""
	Serializer to map the Model instance into JSON format.
	"""

	"""
	Meta class to map serializer's fields with the model fields.
	"""
	genres = fields.MultipleChoiceField(choices=GENRE_CHOICES)
	class Meta:
		model = ImdbScore
		fields = ('id','popularity99', 'director', 'genres', 'imdb_score', 'name','created',)

	def create(self, validated_data):
		return ImdbScore.objects.create(**validated_data)
