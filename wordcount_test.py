import sys

from wordcount2 import main


def run(mode, capsys, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['wordcount2.py', mode, 'letras.txt'])
    main()
    out, _ = capsys.readouterr()
    return out


def test_count(capsys, monkeypatch):
    assert run('--count', capsys,
               monkeypatch) == 'a 2\nb 4\nc 3\nf 1\ng 1\nx 5\ny 1\nz 1'


def test_topcount(capsys, monkeypatch):
    assert run('--topcount', capsys,
               monkeypatch) == 'x 5\nb 4\nc 3\na 2\nf 1\ng 1\nz 1\ny 1'
