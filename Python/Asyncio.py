import time
import asyncio


async def do_some_work(x):    
    print('Started')
    print("Waiting " + str(x))
    await asyncio.sleep(x)
    if x == 12:
        return 'Girish'
    elif x == 1:
        return 'Sancheti'


if __name__ == '__main__':
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(do_some_work(12)), 
             asyncio.ensure_future(do_some_work(1))]
    t0 = time.time()
    a1,a2 = loop.run_until_complete(asyncio.gather(*tasks))
    print('a1:',a1,' a2:',a2)
    print('Completed')
    t1 = time.time()
    print('Took %.4f ms' % (1000*(t1-t0)))
    

