"""
abelfunctions is a Python library for computing with Abelian functions,
algebraic curves, and solving integrable Partial Differential Equations.

The code is available as a git repository at

    https://github.com/cswiercz/abelfunctions

"""
from sage.all import real, imag


def Re(M):
    try:
        return M.apply_map(real)
    except AttributeError:
        return M.real


def Im(M):
    try:
        return M.apply_map(imag)
    except AttributeError:
        return M.imag


from abelfunctions.version import __version__
from abelfunctions.utilities.precision import *
from abelfunctions.abelmap import AbelMap, Jacobian
from abelfunctions.homology import symmetrize_periods
from abelfunctions.puiseux import puiseux
from abelfunctions.riemann_constant_vector import RiemannConstantVector
from abelfunctions.riemann_surface import RiemannSurface
from abelfunctions.riemann_theta.riemann_theta import RiemannTheta

