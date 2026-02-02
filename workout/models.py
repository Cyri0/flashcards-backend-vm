from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name="exercises"
    )
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ("workout", "exercise")

    def __str__(self):
        return f"{self.exercise} – {self.sets}x{self.reps} @ {self.weight} kg"

class WorkoutLog(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.workout} – {self.date}"
