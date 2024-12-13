from rest_framework.views import APIView
from rest_framework.response import Response

class Server(APIView):
    def get(self, request):
        return Response({"status": "Server Running Successfully!"})