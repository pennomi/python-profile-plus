import cProfile
import enum


class Sort(str, enum.Enum):
    """These values come directly from the documentation."""
    calls = 'calls'  # call count
    cumulative = 'cumulative'  # cumulative time
    cumtime = 'cumtime'  # cumulative time
    file = 'file'  # file name
    filename = 'filename'  # file name
    module = 'module'  # file name
    ncalls = 'ncalls'  # call count
    pcalls = 'pcalls'  # primitive call count
    line = 'line'  # line number
    name = 'name'  # function name
    nfl = 'nfl'  # name/file/line
    stdname = 'stdname'  # standard name
    time = 'time'  # internal time
    tottime = 'tottime'  # internal time


class CleanerSort(str, enum.Enum):
    """If we want to clean up naming, I'd propose something super-explicit
    like this.
    """
    call_count = 'calls'
    cumulative_time = 'cumulative'
    filename = 'filename'
    primitive_call_count = 'pcalls'
    line_number = 'line'
    function_name = 'name'
    name_file_line = 'nfl'
    standard_name = 'stdname'  # default
    internal_time = 'time'


class ProfilePlus(cProfile.Profile):
    """Extends the cProfile API with a context manager and uses a different
    (but functionally identical) default kwarg for print_stats.
    """
    def __enter__(self):
        self.enable()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disable()

    def print_stats(self, sort: Sort=Sort.stdname):
        import pstats
        pstats.Stats(self).strip_dirs().sort_stats(sort).print_stats()
