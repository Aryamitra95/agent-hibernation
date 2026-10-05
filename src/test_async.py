import asyncio, time

async def fake_api_call(i):
    await asyncio.sleep(1)
    return i

async def main():
    start = time.time()
    results = await asyncio.gather(*(fake_api_call(i) for i in range(100)))
    print(len(results), "calls finished in", round(time.time() - start, 2), "seconds")

asyncio.run(main())