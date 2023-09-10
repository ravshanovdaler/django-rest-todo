import datetime

from rest_framework import serializers
from .models import Plan


class PlanSerializer(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()
    timeleft = serializers.SerializerMethodField()

    def get_time(self, obj):
        start_date = obj.date_planed_to_start
        end_date = obj.date_planed_to_finish

        if start_date and end_date:
            result = (end_date - start_date).days
            return f"{result} days"
        else:
            return None

    def get_timeleft(self, obj):
        now = datetime.datetime.now()
        planned = obj.date_planed_to_start.replace(tzinfo=None)
        result = abs((now - planned).days)
        return f"{result} days left"

    class Meta:
        model = Plan
        fields = (
            'name', 'description', 'date_created', 'date_planed_to_start', 'date_planed_to_finish', 'image', 'time',
            'timeleft','author')
