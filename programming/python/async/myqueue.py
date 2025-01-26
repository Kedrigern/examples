import asyncio

# vykonání úloh, jejichž argumenty jsou přečteny z fronty
async def task(name, queue):
    print(f"\tCoroutine #{name} started")
    while not queue.empty():
        param = await queue.get()
        print(f"\t\tTask with argument {param : 5.2f} started")
        await asyncio.sleep(5)
        print(f"\t\tTask with argument {param : 5.2f} finished")
    print(f"\tCoroutine #{name} finished")

# funkce, která dokáže dočasně předat řízení přes await
async def main():
    print("Main started")
    queue = asyncio.Queue()

    for i in range(10):
        await queue.put(1 / (i + 1))

    print("Process:", queue)

    # spuštění a čekání na dokončení úloh
    await asyncio.gather(
        asyncio.create_task(task(1, queue)),
        asyncio.create_task(task(2, queue)),
        asyncio.create_task(task(3, queue)),
        asyncio.create_task(task(4, queue)),
        asyncio.create_task(task(5, queue)),
    )
    print("Main finished")

# spuštění funkce, jenž je definována s async
asyncio.run(main())
