from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email','username', 'password','photo']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','photo']



from rest_framework import serializers
from .models import QuizHistory

class QuizHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizHistory
        fields = ['id', 'user', 'domain', 'difficulty_level', 'score', 'attempted_questions', 'submission_time']


from rest_framework import serializers
from .models import QuizQuestion

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ['category', 'difficulty', 'question', 'option_a', 'option_b', 'option_c', 'option_d', 'answer']
