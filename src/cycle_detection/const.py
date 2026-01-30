EPILOG = """\
Input format:
  After running the command, enter N lines, one per vertex.
  Each line: VERTEX NEIGHBOR1 NEIGHBOR2 ...

  VERTEX     - vertex number (integer)
  NEIGHBORx  - adjacent vertices (space-separated integers)

  Vertices with no neighbors: just enter the vertex number.

Examples:
  # Graph with cycle: 1 -> 2 -> 3 -> 1
  $ cycle-detection 3
  1 2
  2 3
  3 1
  YES

  # Graph without cycle: 1 -> 2 -> 3
  $ cycle-detection 3
  1 2
  2 3
  3
  NO

  # Self-loop
  $ cycle-detection 1
  1 1
  YES
"""
