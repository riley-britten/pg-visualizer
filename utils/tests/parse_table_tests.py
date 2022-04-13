from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from utils.parse_table import parse_table

def test_parse_table():
    assert parse_table("[[a, b], [b, a]]") == [[0, 1], [1, 0]], "2 element table fails"

if __name__ == "__main__":
    test_parse_table()
