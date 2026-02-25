import asyncio
import time
from django.http import HttpResponse

# VIEW SÍNCRONA (Exemplo de Blocking Call)
# Esta função trava a execução do servidor durante o tempo de espera.
def contador_sincrono(request):
    time.sleep(3)  # Isso bloqueia a thread
    return HttpResponse("<h1>View Síncrona</h1><p>Contagem bloqueante finalizada.</p>")

# VIEW ASSÍNCRONA (Django Async View)
# Utiliza async/await para liberar o servidor enquanto espera.
async def contador_assincrono(request):
    await asyncio.sleep(3)  # Espera não-bloqueante
    return HttpResponse("<h1>View Assíncrona</h1><p>Contagem não-bloqueante (Async) finalizada!</p>")
