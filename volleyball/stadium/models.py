from django.db import models

# Create your models here.

class Stadium(models.Model):
    name = models.CharField(blank=False, null=False,max_length=50)
    row = models.PositiveIntegerField(blank=False, null=False, default=1)
    seats_in_row = models.PositiveIntegerField(blank=False, null=False, default=10)

    def save(self, *args, **kwargs):
        """Overriding save for adding seats
        Rather than adding seats one by one,Using bulk update to add them all.
        """
        super().save(*args, **kwargs)
        seats = []
        for row_index in range(self.row):
            for column_index in range(self.seats_in_row):
                seats.append(Seat(stadium=self, row=row_index, column=column_index))
        Seat.objects.bulk_create(seats)


class Seat(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    row = models.PositiveIntegerField(blank=False, null=False, default=1)
    column = models.PositiveIntegerField(blank=False, null=False, default=1)