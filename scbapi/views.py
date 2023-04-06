import json
from datetime import datetime, timedelta

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
import jwt
from scbapi.models import User, Barraginha
from scbapi.serializer import ProjetoSerializer


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(name=username, password=password).first()
        if user:
            token = jwt.encode({
                'id': user.id,
                'exp': datetime.utcnow() + timedelta(minutes=30)
            }, 'admin12345').encode('utf-8')

            return JsonResponse({'token': token.decode('utf-8'),'id':user.id})
        else:
            return Response({'error': 'Invalid credentials'},status=404)


class BarraginhaAPIView(APIView):

    def post(self,request,pk):
        name = request.data.get('name')
        latitude = float(request.data.get('latitude'))
        longitude = float(request.data.get('longitude'))
        note = request.data.get('nota')
        pluviosidade_max_anual = float(request.data.get('pluviosidadeMaxAnualDia'))
        area_microbracia_contribuicao =float(request.data.get('areaMicroBacia'))
        maior_cota_microbacia = float(request.data.get('maiorCotaMicroBacia'))
        menor_cota_microbacia = float(request.data.get('menorCotaMicroBacia'))
        comprimento_talvegue_principal = float(request.data.get('talvegue'))
        user = User.objects.get(pk=pk)
        barraginha = Barraginha(user=user, name=name, latitude=latitude, logitude=longitude, note=note,
                                pluviosidade_max_anual=pluviosidade_max_anual,
                                area_microbracia_contribuicao=area_microbracia_contribuicao,
                                maior_cota_microbacia=maior_cota_microbacia,
                                menor_cota_microbacia=menor_cota_microbacia,
                                comprimento_talvegue_principal=comprimento_talvegue_principal)
        barraginha.set_pluviosidade_max_anual_hora()
        barraginha.set_pluviosidade_max_anual_segundo()
        barraginha.set_area_microbacia_contribuicao_ha()
        barraginha.set_declividade_trecho()
        barraginha.set_volume_concentrado_trecho()
        barraginha.set_vazao_escoamento_bruto()
        barraginha.set_vazao_escoamento()
        barraginha.set_tempo_concentracao()
        barraginha.set_tempo_concentracaoo_final()
        barraginha.set_capacidade_infiltracao_a()
        barraginha.set_capacidade_infiltracao_b()
        barraginha.set_velocidadede_infiltracao()
        barraginha.set_quantidade_infiltrar_final()
        barraginha.set_area_total_infiltracao()
        barraginha.set_area_fundo_consider()
        barraginha.save()
        return JsonResponse(status=201, data=None)
    def get(self,request,pk):
        try:
            barraguinhas = Barraginha.objects.filter(user__barraginha=int(pk))
            barraguinhas_json = ProjetoSerializer(barraguinhas,many=True)
            return JsonResponse(barraguinhas_json.data , safe=False)
        except:
            return JsonResponse(status=404,data=None)











def create_user(request):
    pass

def create_barraginha(request):
    pass

def list_barraginha(request):
    pass
    