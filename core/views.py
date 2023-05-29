from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .converter import converter
from .serializers import NumberSerializer
from .converter_tools.errors import (
    NO_DATA_SENT_ERROR,
    INVALID_DATA_ERROR
)


class NumberToText(APIView):
    serializer_class = NumberSerializer
    def get(self, request) -> Response:
        number: str | None = request.GET.get('number')
        if (number != '') and (number != None):
            number = number.strip()
            data: dict = converter(number)
            return Response(data, status=data['status'])
        return Response(NO_DATA_SENT_ERROR, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request) -> Response:
        serializer: NumberSerializer = NumberSerializer(data=request.data)
        if serializer.is_valid():
            number: str | None = serializer.validated_data.get('number')
            if (number != '') and (number != None):
                number = number.strip()
                data: dict = converter(number)
                return Response(data, status=data['status'])
            return Response(NO_DATA_SENT_ERROR, status=status.HTTP_400_BAD_REQUEST)
        return Response(INVALID_DATA_ERROR, status=status.HTTP_400_BAD_REQUEST)
