from rest_framework import serializers

from question.models import Test, TestsQuestionsGroups, QuestionsBase, QuestionsGroup, Question, Answer



class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class TestsQuestionsGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestsQuestionsGroups
        fields = '__all__'


class QuestionsBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsBase
        fields = '__all__'


class QuestionsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsGroup
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
