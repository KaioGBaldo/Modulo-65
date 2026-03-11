import asyncio
import time
from django.http import JsonResponse

# Simulação de um contador ou tarefa pesada síncrona
def contador_sincrono(request):
    start_time = time.time()
    time.sleep(2)  # Chamada bloqueante
    duration = time.time() - start_time
    return JsonResponse({
        "status": "Síncrono finalizado (Bloqueante)",
        "segundos_esperados": 2,
        "duracao_real": round(duration, 2)
    })

# View Assíncrona correta
async def contador_assincrono(request):
    start_time = time.time()
    await asyncio.sleep(2)  # Chamada não-bloqueante
    duration = time.time() - start_time
    return JsonResponse({
        "status": "Assíncrono finalizado (Não-bloqueante)",
        "segundos_esperados": 2,
        "duracao_real": round(duration, 2)
    })