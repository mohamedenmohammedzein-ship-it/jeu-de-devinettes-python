from main import tirer_nombre, comparer


def test_tirer_nombre():
    nombre = tirer_nombre()
    assert 10 <= nombre <= 200


def test_comparer_trop_petit():
    assert comparer(50, 30) == "Trop petit"


def test_comparer_trop_grand():
    assert comparer(50, 70) == "Trop grand"


def test_comparer_trouve():
    assert comparer(50, 50) == "Trouve"
