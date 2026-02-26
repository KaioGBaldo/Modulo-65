import asyncio
import time
from django.http import HttpResponse

# View Síncrona (Exemplo de Blocking Call)
def contador_sincrono(request):
    time.sleep(2) # Trava o servidor por 2 segundos
    return HttpResponse("View Síncrona finalizada (Bloqueante).")

# View Assíncrona (Django Async View)
async def contador_assincrono(request):
    await asyncio.sleep(2) # Espera sem travar o servidor
    return HttpResponse("View Assíncrona finalizada (Não-bloqueante)!")
