#!/usr/bin/env python3
from pathlib import Path
import sys
path_root = Path(Path.cwd()).parent
sys.path.append(str(path_root))

from graphs.graph import graph, power_graph
from utils.parse_table import parse_table

def visualize_graph(g):
    """
    Prints the graph g in tikz format
    """
    print("\\begin{tikzpicture}")

    vertices = [i for i in range(g.size())]
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
            print("")
            print("(" + str(j[0]) + ") -- (" + str(j[1]) + ")", end = "")
    print(";")
    print("\\end{tikzpicture}")

def main():
  if len(sys.argv) < 2:
    print("Usage: graph_visualize -f <file containing multiplication table>")
    return 1 
  elif sys.argv[1] != "-f":
    print ("The only currently supported option is -f")
    return 1
  elif len(sys.argv) < 3:
    print ("Usage: graph_visualize -f <file containing multiplication table>")
    return 1
  f = open(sys.argv[2], "r")
  table = f.read()
  table = parse_table(table)
  G = power_graph(table)
  visualize_graph(G)
  return 0

if __name__ == "__main__":
  main()
