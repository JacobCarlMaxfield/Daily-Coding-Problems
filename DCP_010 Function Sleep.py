"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
import time

def f(n):
    print('I slept for {} milliseconds!'.format(n))


def job_scheduler(func, n):
    time.sleep(n/1000)
    f(n)


job_scheduler(f, 3000)