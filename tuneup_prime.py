import cProfile
import pstats
import functools
import timeit
import io

def profile(func):
    @functools.wraps(func)
    def wrapper_function(*args, **kwargs):
        profile_object = cProfile.Profile()
        profile_object.enable
        result = func(*args, **kwargs)
        profile_object.disable
        # s = io.StringIO()
        # sortby="cumulative"
        # ps = pstats.Stats(profile_object, stream=s).sort_stats(sortby)
        # ps.print_stats()
        # print(s.getvalue())
        stats_object = pstats.Stats(profile_object)
        stats_object.strip_dirs()
        stats_object.sort_stats("cumulative")
        stats_object.print_stats()
        return result
    return wrapper_function()

def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie == title:
            return True
    return False

@profile
def find_duplicate_movies(src='movies.txt'):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]
    duplicates = []
    while movies:
        movie = movies.pop()
        if movie in movies:
            duplicates.append(movie)
    return duplicates

def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))

def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    # print("setdefault :", end = " ")
    t  = timeit.Timer(stmt="src", setup="setup")
    result = t.repeat(repeat=7,  number=3)
    return result

if __name__ == '__main__':
    main()