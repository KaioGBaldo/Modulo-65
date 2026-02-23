import asyncio
import time
from django.http import JsonResponse # Usando JsonResponse já que a loja é sua API

# VIEW SÍNCRONA (Exemplo de Blocking Call solicitada)
def contador_sincrono(request):
    time.sleep(3)  # Isso bloqueia o servidor
    return JsonResponse({"status": "Síncrono finalizado", "mensagem": "Esta foi uma blocking call."})

# VIEW ASSÍNCRONA (Django Async View solicitada)
async def contador_assincrono(request):
    await asyncio.sleep(3)  # Isso NÃO bloqueia o servidor
    return JsonResponse({"status": "Assíncrono finalizado", "mensagem": "Executado sem bloquear outras requisições!"})
