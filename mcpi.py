import math
import random

def linspace(start, stop, num):
    out = []
    for i in range(num):
        out.append(start + i/num)
    return out

# Returns a tuple (x, y)
# where x is a random value in range rx
# and y is a random value in range ry
def get_random_point(rx, ry):
    x = random.choice(rx)
    y = random.choice(ry)
    return (x, y)

def norm(v):
    return math.sqrt(v[0] ** 2 + v[1] ** 2)

# Returns a PI approximation using 
# monte-carlo method, with N random points
def monte_carlo_pi(N, divisions = 64*4096):
    circle = 0
    total = 0

    rx = linspace(-1, 1, divisions)
    ry = rx

    for i in range(N):
        v = get_random_point(rx, ry)
        r = norm(v)

        total += 1
        if(r < 1):
            circle += 1

    ratio = circle / total

    return 4 * ratio
