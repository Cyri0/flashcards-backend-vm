from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Exercise, Workout, WorkoutExercise, WorkoutLog
from .serializers import (
    ExerciseSerializer,
    WorkoutSerializer,
    WorkoutExerciseSerializer,
    WorkoutLogSerializer,
)

@api_view(["GET", "POST"])
def exercise_list(request):
    if request.method == "GET":
        serializer = ExerciseSerializer(Exercise.objects.all(), many=True)
        return Response(serializer.data)

    serializer = ExerciseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def exercise_detail(request, pk):
    try:
        exercise = Exercise.objects.get(pk=pk)
    except Exercise.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(ExerciseSerializer(exercise).data)

    if request.method == "PUT":
        serializer = ExerciseSerializer(exercise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    exercise.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def workout_list(request):
    if request.method == "GET":
        serializer = WorkoutSerializer(Workout.objects.all(), many=True)
        return Response(serializer.data)

    serializer = WorkoutSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def workout_detail(request, pk):
    try:
        workout = Workout.objects.get(pk=pk)
    except Workout.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(WorkoutSerializer(workout).data)

    if request.method == "PUT":
        serializer = WorkoutSerializer(workout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    workout.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def add_exercise_to_workout(request):
    serializer = WorkoutExerciseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT", "DELETE"])
def workout_exercise_detail(request, pk):
    try:
        we = WorkoutExercise.objects.get(pk=pk)
    except WorkoutExercise.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = WorkoutExerciseSerializer(we, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    we.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def workout_log_list(request):
    if request.method == "GET":
        serializer = WorkoutLogSerializer(
            WorkoutLog.objects.order_by("-date"),
            many=True
        )
        return Response(serializer.data)

    serializer = WorkoutLogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
