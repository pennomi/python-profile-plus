import cProfile
import io
import pstats
import requests

from profile_plus import ProfilePlus, Sort


def fib(n):
    """Inefficient, recursive fibonacci sequence."""
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)


def main():
    # The old way, directly from the docs
    pr = cProfile.Profile()
    pr.enable()
    requests.get("https://www.python.org")
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())

    # Proposed way (using pure-Python prototype)
    with ProfilePlus() as pr:
        requests.get("https://www.python.org")
    pr.print_stats(sort=Sort.cumulative)


if __name__ == "__main__":
    main()
