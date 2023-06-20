from math import sqrt
from typing import Union

def solve(a: float, b: float, c: float, e: float=1e-5) -> Union[float, float]:
    if abs(a) <= e:
        raise ValueError("Argument a shouldn't be 0")
    
    d = b*b - 4*a*c

    if  d < -e:
        return []
    elif abs(d) <= e:
        return [-b/2*a, -b/2*a]
    elif d > e:
        x1 = (-b + sqrt(d)) / 2*a
        x2 = (-b - sqrt(d)) / 2*a
        return [x1, x2]

