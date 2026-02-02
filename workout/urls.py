from django.urls import path
from . import views

urlpatterns = [
    path("exercises/", views.exercise_list),
    path("exercises/<int:pk>/", views.exercise_detail),

    path("workouts/", views.workout_list),
    path("workouts/<int:pk>/", views.workout_detail),

    path("workout-exercises/", views.add_exercise_to_workout),
    path("workout-exercises/<int:pk>/", views.workout_exercise_detail),

    path("workout-logs/", views.workout_log_list),
]
