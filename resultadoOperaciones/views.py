from rest_framework.views import APIView
from rest_framework.response import Response


class Resultados(APIView):
    """Probar la vista del API"""

    def get(self, request, format=None):
        """ Regresa una lista de atributos de APIView"""
        una_vista = [
            'Estamos usando un método HTTP como función (get, post, patch, put, delete)',
            'Es muy similar a las vistas de Django',
            'Nos da el mayor control sobre la lógica de la aplicación',
            'Está mapeado a los URLs',
        ]

        return Response({'message': 'Exito!', 'una_vista': una_vista})
