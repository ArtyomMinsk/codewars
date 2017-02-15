import reverse_string as r


def test_reverse_string():
    string = "revolver"
    assert r.reverse_string(string) == "revlover"
