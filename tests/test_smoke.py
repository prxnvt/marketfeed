import marketfeed


def test_version_is_exposed() -> None:
    assert marketfeed.__version__ == "0.1.0"