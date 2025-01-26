"""
Basic usage of asyncio module
"""

import asyncio

async def task(name: str, timeout: int = 1) -> None:
    print(f"Task {name} started")
    await asyncio.sleep(timeout)
    print(f"Task {name} finished")

async def main() -> None:
    print("Begin main")

    task1 = asyncio.create_task(task("first", 2))
    task2 = asyncio.create_task(task("second"))
    task3 = asyncio.create_task(task("third"))

    await asyncio.gather(task1, task2, task3)

    print("Done")

asyncio.run(main())
