from rest_framework.views import APIView
from rest_framework.response import Response

class Running(APIView):
    def get(self, request):
        return Response({"status": "Server Running Successfully!"})