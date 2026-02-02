from django.urls import path
from . import views

urlpatterns = [
    path("api/exercises/", views.exercise_list),
    path("api/exercises/<int:pk>/", views.exercise_detail),

    path("api/workouts/", views.workout_list),
    path("api/workouts/<int:pk>/", views.workout_detail),

    path("api/workout-exercises/", views.add_exercise_to_workout),
    path("api/workout-exercises/<int:pk>/", views.workout_exercise_detail),

    path("api/workout-logs/", views.workout_log_list),
]
