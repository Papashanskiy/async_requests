import asyncio
import time
import aiohttp


async def get_uuid(session):
    url = 'http://127.0.0.1:8000/api/random-uuid'

    async with sema, session.get(url) as response:
        return await response.json()


async def async_main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        results = await asyncio.gather(*[get_uuid(session) for _ in range(1000)])
        return results


if __name__ == '__main__':
    sema = asyncio.BoundedSemaphore(30)

    event_loop = asyncio.get_event_loop()
    start = time.time()

    result = event_loop.run_until_complete(async_main(event_loop))

    end = time.time()

    total = end - start
    print(end - start)

    print(result)
