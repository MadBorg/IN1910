from vector import Vector


def test_str():
    u = Vector(0, 4, -2)
    assert str(u) == "(0, 4, -2)"

    v = Vector(0, 4)
    assert str(u) == "(0, 4)"


def test_repr():
    u = Vector(0, 4, -2)
    assert repr(u) == "Vector(0, 4, -2)"

    v = Vector(0, 4)
    assert str(u) == "Vector(0, 4)"


def test_add():
    u = Vector(2, 0, -2)
    v = Vector(2, 4, 2)
    assert u + v == Vector(4, 4, 0)


def test_sub():
    u = Vector(2, 0, -2)
    v = Vector(2, 4, 2)
    assert u - v == Vector(0, -4, -4)


def test_dot():
    u = Vector(2, 0, -2)
    v = Vector(2, 4, 2)
    assert u.dot(v) == (4 + 0 - 4)


def test_mul():
    u = Vector(2, 0, -2)
    v = Vector(2, 4, 2)
    assert u * v == (4 + 0 - 4)


def test_cross():
    u = Vector(2, 0, -2)
    v = Vector(2, 4, 2)
    assert u.cross(v) == Vector(8, -8, 8)


def test_matmul():
    u = Vector(2, 0, -2)
    v = Vector(2, 4, 2)
    assert u @ v == Vector(8, -8, 8)


def test_perpendicular():

    u = Vector(2, 0, -2)
    v = Vector(2, 4, 2)
    assert u.perpendicular(v)

    w = u @ v
    assert w.perpendicular(u)
    assert w.perpendicular(v)


def test_scalarmult_right():

    u = Vector(4, -6, 2)
    assert u * 2 == Vector(8, -12, 4)


def test_scalarmult_left():

    u = Vector(4, -6, 2)
    assert 2 * u == Vector(8, -12, 4)


def test_get_length():
    u = Vector(4, 0, 0)
    assert u.length == 4


def test_set_length():
    u = Vector(4, 0, 0)
    u.length = 1
    assert u == Vector(1, 0, 0)


def test_unit_vector():

    u = Vector(2, -2, 1)
    w = u.unit()

    assert w.length == 1
    assert not (u is w)


def test_dim():
    u = Vector(1, 0)
    assert u.dim == 2
    assert len(u) == 2

    v = Vector(0, 1, 0)
    assert v.dim == 3
    assert len(v) == 3


if __name__ == "__main__":
    test_str()
    test_repr()
    test_add()
    test_sub()
    test_dot()
    test_cross()
    test_mul()
    test_matmul()
    test_perpendicular()
    test_scalarmult_right()
    test_scalarmult_left()
    test_get_length()
    test_set_length()
    test_unit_vector()
    test_dim()
