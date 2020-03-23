#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "mprodhan/yabamov"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    def wrapper_function(*args, **kwargs):
        profile_object = cProfile.Profile()
        profile_object.enable()
        result = func(*args, **kwargs)
        profile_object.disable()
        sortby="cumulative"
        ps = pstats.Stats(profile_object).strip_dirs().sort_stats(sortby)
        ps.print_stats(10)
        return result
    return wrapper_function

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
    movies.sort()
    duplicates = [movie1 for movie1, movie2 in zip(movies[:-1], movies[1:]) if movie1 == movie2]
    return duplicates

def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))

def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    print("setdefault :", end = " ")
    t  = timeit.Timer(stmt="src", setup="from __main__ import find duplicate_movies")
    result = t.repeat(repeat=7,  number=3)
    return result

if __name__ == '__main__':
    main()