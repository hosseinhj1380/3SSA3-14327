
from .models import Reservation,Table


def get_available_table(start,end):
    reserved_table_ids = Reservation.objects.filter(
    start_time__lt=end,
    end_time__gt=start
    ).values_list('table__id', flat=True)


    return Table.objects.exclude(
        id__in=reserved_table_ids
    )
