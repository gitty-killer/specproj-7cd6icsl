from etl.pipeline import run


def test_run():
    out = run(['A\n', 'b\n'])
    assert out == ['a', 'b']
