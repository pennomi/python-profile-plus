import cProfile
import io
import pstats
import requests

from profile_plus import ProfilePlus, Sort


def main():
    # The normal way, directly from the docs
    # Note that it uses an io stream which I'm not doing below.
    pr = cProfile.Profile()
    pr.enable()
    requests.get("https://www.python.org")  # do something interesting
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())

    # Proposed way (using the pure-Python prototype)
    with ProfilePlus() as pr:
        requests.get("https://www.python.org")  # do something interesting
    pr.print_stats(sort=Sort.cumulative)


if __name__ == "__main__":
    main()
