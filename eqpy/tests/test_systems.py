import sympy
from eqpy._systems import BaseSystem, System
from eqpy._utils import raises


def test_symbol_types():
    A = System()
    assert A.x is A.x
    assert isinstance(A.x, sympy.Symbol)
    assert A[1] is A[1]
    assert isinstance(A[1], sympy.Dummy)
    B = System()
    assert A.x is B.x
    assert A[1] is not B[1]
    C = System(dummies=True)
    assert isinstance(C.x, sympy.Dummy)
    assert isinstance(C[1], sympy.Dummy)
    D = System(dummies=['x'])
    assert isinstance(D.x, sympy.Dummy)
    assert isinstance(D.y, sympy.Symbol)
    assert isinstance(D[1], sympy.Dummy)
    E = System(dummies=False)
    assert isinstance(E.x, sympy.Symbol)
    assert isinstance(E[1], sympy.Dummy)


def test_prefix():
    A = System()
    B = System(prefix='B_')
    assert A.B_x is B.x
    assert str(B.x) == 'B_x'
    assert str(B[0]) == '_B_0'
    C = System(prefix='C_', prefix_include=['x', 1, '2'])
    assert str(C.x) == 'C_x'
    assert str(C.y) == 'y'
    assert str(C[0]) == '_0'
    assert str(C[1]) == '_C_1'
    assert str(C[2]) == '_2'
    D = System(prefix='D_', prefix_exclude=['x', 1, '2'])
    assert str(D.x) == 'x'
    assert str(D.y) == 'D_y'
    assert str(D[0]) == '_D_0'
    assert str(D[1]) == '_1'
    assert str(D[2]) == '_D_2'
    assert raises(ValueError, lambda: System(prefix='A_', prefix_include=['x'],
                                             prefix_exclude=['y']))


def test_suffix():
    A = System()
    B = System(suffix='_B')
    assert A.x_B is B.x
    assert str(B.x) == 'x_B'
    assert str(B[0]) == '_0_B'
    C = System(suffix='_C', suffix_include=['x', 1, '2'])
    assert str(C.x) == 'x_C'
    assert str(C.y) == 'y'
    assert str(C[0]) == '_0'
    assert str(C[1]) == '_1_C'
    assert str(C[2]) == '_2'
    D = System(suffix='_D', suffix_exclude=['x', 1, '2'])
    assert str(D.x) == 'x'
    assert str(D.y) == 'y_D'
    assert str(D[0]) == '_0_D'
    assert str(D[1]) == '_1'
    assert str(D[2]) == '_2_D'
    assert raises(ValueError, lambda: System(suffix='_A', suffix_include=['x'],
                                             suffix_exclude=['y']))


def test_slice_get():
    A = System()
    x0, x1 = A[:2]
    assert x0 is A[0]
    assert x1 is A[1]
    y1, y2 = A[1:3]
    assert y1 is x1
    z0, z2 = A[:3:2]
    assert z2 is y2
    z2, z4 = A[2:5:2]
    assert z2 is y2
    z2, z1 = A[2:0:-1]
    assert z2 is y2
    assert raises(ValueError, lambda: A[0::2])
    assert raises(ValueError, lambda: A[::2])
    assert raises(ValueError, lambda: A[0::])
    assert raises(ValueError, lambda: A[::])


def test_equations():
    A = System()
    A.x = 2*A.y
    assert A[...].equations[A.x] == [sympy.Eq(A.x, 2*A.y)]
    assert A[A.x] == [sympy.Eq(A.x, 2*A.y)]
    A[A.x] = 20*A.y
    assert A[A.x] == [sympy.Eq(A.x, 20*A.y)]
    A.x = sympy.Eq(2*A.y, 3*A.z)
    assert A[A.x] == [sympy.Eq(A.x, 2*A.y), sympy.Eq(A.x, 3*A.z)]
    A.x = (4*A.x1, 5*A.x2, 6*A.x3)
    assert A[A.x] == [sympy.Eq(A.x, 4*A.x1), sympy.Eq(A.x, 5*A.x2),
                      sympy.Eq(A.x, 6*A.x3)]
    A[1] = 2*A.x
    assert A[...].equations[A[1]] == [sympy.Eq(A[1], 2*A.x)]
    assert A[A[1]] == [sympy.Eq(A[1], 2*A.x)]
    A[A[1]] = 20*A.x
    assert A[A[1]] == [sympy.Eq(A[1], 20*A.x)]


def test_equations_slice():
    A = System()
    A[0:3] = (2*A.x, 3*A.y, 4*A.z)
    assert A[A[0]] == [sympy.Eq(A[0], 2*A.x)]
    assert A[A[1]] == [sympy.Eq(A[1], 3*A.y)]
    assert A[A[2]] == [sympy.Eq(A[2], 4*A.z)]
    A[1:6:2] = (20*A.x, 30*A.y, 40*A.z)
    assert A[A[1]] == [sympy.Eq(A[1], 20*A.x)]
    assert A[A[3]] == [sympy.Eq(A[3], 30*A.y)]
    assert A[A[5]] == [sympy.Eq(A[5], 40*A.z)]

    def badassign():
        A[0:3] = (2*A.x, 3*A.y)
    assert raises(ValueError, badassign)

    def badassign():
        A[0:3] = (2*A.x, 3*A.y, 4*A.x, 5*A.y)
    assert raises(ValueError, badassign)

    def badassign():
        A[0:] = (2*A.x, 3*A.y)
    assert raises(ValueError, badassign)


def test_userdict():
    A = System()
    A['x'] = 5
    A.x = 4
    assert A['x'] == 5
    assert isinstance(A[A.x][0], sympy.Equality)
    A['1'] = 6
    A[1] = 7
    assert A['1'] == 6
    assert isinstance(A[A[1]][0], sympy.Equality)


def test_iter():
    A = System()
    A.x1 = 2*A.y1
    A.x1 = 2*A.y1
    A.x2 = [3*A.y2]
    A.x3 = [4*A.y3a, 5*A.y3b, 6*A.y3c]
    A.x4 = sympy.Eq(A.y4a, 2*A.y4b)
    A[1] = 2*A.z1
    A[1] = 2*A.z1
    A[2] = [3*A.z2]
    A[3] = [4*A.z3a, 5*A.z3b, 6*A.z3c]
    A[4] = sympy.Eq(A.z4a, 2*A.z4b)
    count = 0
    seen = set()
    for eq in A:
        assert isinstance(eq, sympy.Equality)
        assert eq not in seen
        seen.add(eq)
        count += 1
    assert count == 14


def test_contains():
    A = System()
    A.x = 2*A.y
    A['z'] = 'zee'
    A[1] = 3*A[2]
    A['3'] = 'three'
    assert A.x in A
    assert A.y not in A
    assert 'z' in A
    assert 'zee' not in A
    assert A[1] in A
    assert A[2] not in A
    assert '3' in A
    assert 'three' not in A


def test_assumptions():
    A = System()
    A(A.x > 0)
