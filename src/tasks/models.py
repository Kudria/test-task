from django.db import models


class Task(models.Model):
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

    STATUS_CHOICES = {
        IN_PROGRESS: 'In Progress',
        COMPLETED: 'Completed',
    }

    text = models.TextField(
        verbose_name="Text",
    )

    status = models.CharField(
        verbose_name="Status",
        max_length=16,
        choices=STATUS_CHOICES,
        default=IN_PROGRESS,
    )

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.text[:25]