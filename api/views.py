import asyncio
import time
from django.http import HttpResponse

# VIEW SÍNCRONA (Exemplo de Blocking Call)
# Esta view utiliza time.sleep, que trava a thread do servidor.
# Enquanto ela executa, o servidor não consegue processar outras requisições nesta thread.
def contador_sincrono(request):
    time.sleep(3)  # Isso é uma blocking call
    return HttpResponse("<h1>View Síncrona</h1><p>Resultado após 3 segundos de bloqueio total.</p>")

# VIEW ASSÍNCRONA (Django Async View)
# Requisito: Utilizar 'async def' e 'await'.
# O asyncio.sleep não bloqueia a thread, permitindo que o Django lide com outras tarefas.
async def contador_assincrono(request):
    await asyncio.sleep(3)  # Espera não-bloqueante
    return HttpResponse("<h1>View Assíncrona</h1><p>Resultado após 3 segundos sem bloquear o servidor!</p>")
