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
  directed = False
  options = []

  if len(sys.argv) < 2:
    print("Usage: graph_visualize -f <file containing multiplication table>\n" +
            "or graph_visualize \"<TABLE>\"")
    return 1 

  # Parse command line options
  for i in range(1, len(sys.argv) - 1):
    options.append(sys.argv[i])

  if "-d" in options:
    directed = True
 
  if "-f" in options:
    f = open(sys.argv[len(sys.argv) - 1], "r")
    table = parse_table(f.read())
  else:
    print("Table to parse " + sys.argv[len(sys.argv) - 1])
    table = parse_table(sys.argv[len(sys.argv) - 1])

  G = power_graph(table, directed)
  visualize_graph(G)
  return 0

if __name__ == "__main__":
  main()
