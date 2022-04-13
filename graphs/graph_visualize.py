from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

from graphs.graph import graph

def visualize_graph(g):
    """
    Prints the graph g in tikz format
    """
    print("\\begin{tikzpicture}")

    vertices = [i + 1 for i in range(g.size())]
    for i in vertices:
        print("\\node (" + str(i) + ") at (" + str(i%2) + ", " +
            str(i//2) + "){$" + str(i) + "$};")

    print("")

    if g.is_directed():
        print("\\draw[->]", end = "")
        for j in g.get_edges():
            print("")
            print("(" + str(j[0]) + ") edge (" + str(j[1]) + ")", end = "")
    else:
        print("\\draw", end = "")
        for j in g.get_edges():
            print("(" + str(j[0]) + ") -- (" + str(j[1]) + ")", end = "")
    print(";")
    print("\\end{tikzpicture}")
