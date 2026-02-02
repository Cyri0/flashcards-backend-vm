from rest_framework import serializers
from .models import Exercise, Workout, WorkoutExercise, WorkoutLog

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise_name = serializers.CharField(
        source="exercise.name",
        read_only=True
    )

    class Meta:
        model = WorkoutExercise
        fields = [
            "id",
            "exercise",
            "exercise_name",
            "sets",
            "reps",
            "weight",
        ]

class WorkoutSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = [
            "id",
            "name",
            "exercises",
        ]

class WorkoutLogSerializer(serializers.ModelSerializer):
    workout_name = serializers.CharField(
        source="workout.name",
        read_only=True
    )

    class Meta:
        model = WorkoutLog
        fields = [
            "id",
            "workout",
            "workout_name",
            "date",
            "notes",
        ]
