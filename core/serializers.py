from rest_framework import serializers

class NumberSerializer(serializers.Serializer):
    number = serializers.CharField(
        max_length=(10**36),
        required=True,
    )
