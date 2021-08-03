from score.api.roles import request_query_cpf, verify_validation
from score.api.serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from score.models import Person

class person_detail(APIView):
    def verify_scale(self, request):
        data = request
        try:
            data['scale']
            return data
        except KeyError:
            data['scale'] = 'error'
            return data


    def verify_cpf(self, request):
        data = request.data
        try:
            data['cpf']
            return data
        except KeyError:
            data['cpf'] = 'error'
            return data


    def post(self, request):
        data = self.verify_cpf(request)
        try:
            if data['cpf'] != 'error':
                if len(data['cpf']) == 14:
                    person = Person.objects.get(cpf=data['cpf'])
                    serializer = PersonSerializer(person)
                    return Response(serializer.data, status=status.HTTP_200_OK)

                msg = {'Cpf': 'Verifique a formatação correta de CPF(xxx.xxx.xxx-xx) e tente novamente.'}
                return Response(msg, status=status.HTTP_404_NOT_FOUND)

            return Response({"Cpf":"Envie um número de CPF!"}, status=status.HTTP_400_BAD_REQUEST)

        except Person.DoesNotExist:
            data = self.verify_scale(request.data)

            if data['scale'] != 'error' and data['scale'] in [1, 10, 100, 1000]:
                if verify_validation:
                    data['score'] = request_query_cpf(data['cpf'], data['scale'])
                    serializer = PersonSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)

                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            msg = {"Scale":"Por favor, envie uma escala válida."}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

            

    def patch(self, request):
        data = self.verify_cpf(request)
        data = self.verify_scale(data)
        if data['cpf'] != 'error':
            try:
                person = Person.objects.get(cpf=data['cpf'])
                if data['cpf'] != person.cpf:
                    message = { "Mensagem": "Você não pode modificar o CPF, apenas a escala!"}
                    return Response(message, status=status.HTTP_401_UNAUTHORIZED)

                if data['scale'] != person.scale:
                    data['score'] = request_query_cpf(data['cpf'], data['scale'])

                serializer = PersonSerializer(person, data=data)
                if serializer.is_valid():
                      serializer.save()
                      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

                return Response({"Scale": "Por favor, envie uma escala válida."}, status=status.HTTP_400_BAD_REQUEST)
            except Person.DoesNotExist:
                return Response({'cpf': 'Não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        return Response({"Cpf":"Envie um número de CPF!"}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request):
        data = self.verify_cpf(request)
        if data['cpf'] != 'error':
            try:
                person = Person.objects.get(cpf=data['cpf'])
                person.delete()

                return Response(status=status.HTTP_204_NO_CONTENT)
            except Person.DoesNotExist:
                return Response({"Cpf":"Número de CPF não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        return Response({"Cpf":"Envie um número de CPF!"}, status=status.HTTP_404_NOT_FOUND)
