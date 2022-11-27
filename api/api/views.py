import uuid
import asyncio
import datetime

from django.http import JsonResponse


async def random_uuid(request):
    await asyncio.sleep(2)
    return JsonResponse({'uuid': uuid.uuid4(), 'now': datetime.datetime.now().strftime('%H:%M:%S')})
