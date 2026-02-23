import asyncio
import time
from django.http import HttpResponse

# VIEW SÍNCRONA (Exemplo de Blocking Call)
# Esta função trava o servidor enquanto espera.
def contador_sincrono(request):
    time.sleep(3)  # Bloqueia a thread
    return HttpResponse("View Síncrona finalizada (Bloqueante)")

# VIEW ASSÍNCRONA (Django Async View)
# Requisito: async def + await
# Esta função libera o servidor para outras tarefas enquanto espera.
async def contador_assincrono(request):
    await asyncio.sleep(3)  # Não bloqueia a thread
    return HttpResponse("View Assíncrona finalizada (Não-bloqueante)")
