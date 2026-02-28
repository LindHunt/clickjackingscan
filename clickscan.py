#!/usr/bin/env python3

"""
LINDHUNT Clickjacking Scanner
Author: LINDHUNT
Version: 2.0
"""

import argparse
import asyncio
import aiohttp
import ssl
from colorama import Fore, Style, init

init(autoreset=True)

__version__ = "2.0"
__author__ = "LINDHUNT"

BANNER = f"""{Fore.CYAN}
██╗     ██╗███╗   ██╗██████╗ ██╗  ██╗██╗   ██╗███╗   ██╗████████╗
██║     ██║████╗  ██║██╔══██╗██║  ██║██║   ██║████╗  ██║╚══██╔══╝
██║     ██║██╔██╗ ██║██║  ██║███████║██║   ██║██╔██╗ ██║   ██║   
██║     ██║██║╚██╗██║██║  ██║██╔══██║██║   ██║██║╚██╗██║   ██║   
███████╗██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║ ╚████║   ██║   
╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   

{Style.RESET_ALL}{Fore.YELLOW}Clickjacking Intelligence Scanner | v{__version__}{Style.RESET_ALL}
"""

USER_AGENT = "LINDHUNT-Scanner/2.0"
stats = {"protected": 0, "vulnerable": 0, "error": 0}


def normalize_url(url):
    if not url.startswith("http"):
        return "https://" + url
    return url


async def analyze_target(session, url):
    try:
        url = normalize_url(url.strip())

        async with session.get(url, timeout=8) as response:
            headers = response.headers

            xfo = headers.get("X-Frame-Options")
            csp = headers.get("Content-Security-Policy")

            if xfo:
                stats["protected"] += 1
                return f"{Fore.GREEN}[PROTECTED]{Style.RESET_ALL} {url} | XFO: {xfo}"

            if csp and "frame-ancestors" in csp:
                stats["protected"] += 1
                return f"{Fore.GREEN}[PROTECTED]{Style.RESET_ALL} {url} | CSP frame-ancestors"

            stats["vulnerable"] += 1
            return f"{Fore.RED}[VULNERABLE]{Style.RESET_ALL} {url} | No anti-clickjacking headers"

    except Exception:
        stats["error"] += 1
        return f"{Fore.MAGENTA}[ERROR]{Style.RESET_ALL} {url}"


async def run_scan(targets, output=None):
    ssl_context = ssl.create_default_context()
    connector = aiohttp.TCPConnector(ssl=ssl_context)

    async with aiohttp.ClientSession(
        connector=connector,
        headers={"User-Agent": USER_AGENT}
    ) as session:

        tasks = [analyze_target(session, t) for t in targets if t.strip()]
        results = await asyncio.gather(*tasks)

        for result in results:
            print(result)

        print("\n" + "-" * 60)
        print(f"{Fore.GREEN}Protected:{Style.RESET_ALL} {stats['protected']}")
        print(f"{Fore.RED}Vulnerable:{Style.RESET_ALL} {stats['vulnerable']}")
        print(f"{Fore.MAGENTA}Errors:{Style.RESET_ALL} {stats['error']}")

        if output:
            clean_results = [
                r.replace(Fore.GREEN, "")
                 .replace(Fore.RED, "")
                 .replace(Fore.MAGENTA, "")
                 .replace(Style.RESET_ALL, "")
                for r in results
            ]
            with open(output, "w") as f:
                f.write("\n".join(clean_results))


def main():
    print(BANNER)

    parser = argparse.ArgumentParser(description="LINDHUNT Clickjacking Scanner")
    parser.add_argument("-u", help="Single target URL")
    parser.add_argument("-list", help="File containing multiple targets")
    parser.add_argument("-o", help="Save output to file")

    args = parser.parse_args()

    if args.u:
        asyncio.run(run_scan([args.u], args.o))

    elif args.list:
        try:
            with open(args.list, "r") as f:
                targets = f.readlines()
            asyncio.run(run_scan(targets, args.o))
        except Exception:
            print(f"{Fore.RED}Failed to read target list file.{Style.RESET_ALL}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
