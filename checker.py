import sys
import requests

def check_urls(urls):
    failed = False

    for url in urls:
        try:
            res = requests.get(url, timeout=5)
            print(f"{url} -> {res.status_code}")

            if res.status_code != 200:
                failed = True

        except Exception as e:
            print(f"{url} -> ERROR: {e}")
            failed = True

    return failed


if __name__ == "__main__":
    urls = sys.argv[1:]

    if not urls:
        print("Usage: python checker.py <url1> <url2>")
        sys.exit(1)

    failed = check_urls(urls)

    if failed:
        sys.exit(1)
