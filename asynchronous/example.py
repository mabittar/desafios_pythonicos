import asyncio
from re import L
import time

def sync_count(num: int):
    print(f'One with sleep_time {num}')
    time.sleep(num)
    print(f'Two with sleep_time {num}')

def sync_main():
    for num in (2, 1, 3):
        sync_count(num)
        

async def async_count(num: int):
    print(f'One with sleep_time {num}')
    await asyncio.sleep(num)
    print(f'Two with sleep_time {num}')
    
async def async_main():
    await asyncio.gather(async_count(2), async_count(1), async_count(3))


if __name__ == '__main__':
    print(f'Start synchronous routine')
    start = time.time()
    sync_main()
    end = time.time()
    elapsed = end - start
    print(f'Executed synchronous routine in {elapsed:0.2f} seconds.')
    
    print(f'Start asynchronous routine')
    start = time.time()
    asyncio.run(async_main())
    end = time.time()
    elapsed = end - start
    print(f'Executed asynchronous routine in {elapsed:0.2f} seconds.')
