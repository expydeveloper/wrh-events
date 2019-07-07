import django_filters
from django_filters import rest_framework as filters

from apps.membership.models import Event, Race, RaceResult


class EventFilter(filters.FilterSet):
    start_date_min = django_filters.DateFilter(field_name='start_date', lookup_expr='gte', required=False)
    start_date_max = django_filters.DateFilter(field_name='start_date', lookup_expr='lte', required=False)
    end_date_min = django_filters.DateFilter(field_name='end_date', lookup_expr='gte', required=False)
    end_date_max = django_filters.DateFilter(field_name='end_date', lookup_expr='lte', required=False)

    class Meta:
        model = Event
        exclude = ('event_flyer', 'image')


class RaceFilter(filters.FilterSet):

    class Meta:
        model = Race
        fields = '__all__'


class RaceResultFilter(filters.FilterSet):

    class Meta:
        model = RaceResult
        fields = '__all__'
