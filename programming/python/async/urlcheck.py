#!/usr/bin/python3
"""
Checks bunch of urls
"""

import asyncio
import requests

async def checkUrl(url: str) -> None:

    code: int = 0

    try:
        code = requests.get(url).status_code
    except requests.exceptions.ConnectionError:
        print(f"[FAIL] connection error to domain {url}")
        return

    match code:
        case 200:
            print(f"[OK] {url}")
        case 300:
            print(f"[WARN] redirected {url}") # But to where?
        case _:
             print(f"[FAIL] bad code: {code} for {url}")


async def main() -> None:
    urls: list[str] = [
        "https://httpstat.us/200",
        "https://httpstat.us/300",
        "https://httpstat.us/400",
        "https://httpstat.us/500",
        "https://www.python.org/",
        "https://www.python.cz/",
        "https://pythex.org/",
        "https://pyladies.cz/",
        "https://pyladies.czz/"
    ]

    tasks: list[asyncio.Task] = []

    for url in urls:
        tasks.append(asyncio.create_task(checkUrl(url)))

    await asyncio.gather(*tasks)

asyncio.run(main())
