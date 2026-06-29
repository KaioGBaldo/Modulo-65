import asyncio
from django.http import JsonResponse

# Um contador global simples para fins demonstrativos da view
contador_acessos = 0

async def async_counter_view(request):
    """
    View Assíncrona que demonstra conceitos de Non-blocking calls.
    Utiliza asyncio.sleep para não travar a execução do servidor.
    """
    global contador_acessos
    
    # Simula uma operação assíncrona/I-O bound (ex: busca em API externa ou processo lento)
    # Sem efetuar uma blocking call convencional
    await asyncio.sleep(1) 
    
    contador_acessos += 1
    
    return JsonResponse({
        "status": "sucesso",
        "mensagem": "Operação assíncrona executada com sucesso!",
        "contador_total_acessos": contador_acessos
    })
