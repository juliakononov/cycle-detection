import argparse
import sys

from cycle_detection import has_cycle
from cycle_detection.const import EPILOG
from cycle_detection.misc import validate_non_negative


class ParseError(Exception):
    """Raised when input parsing fails."""
    pass


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Detect cycles in a directed graph.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=EPILOG,
    )

    parser.add_argument(
        "n",
        type=int,
        help="number of vertices",
    )

    return parser

@validate_non_negative
def parse_args() -> int:
    parser = create_parser()
    args = parser.parse_args()

    return args.n


def parse_adjacency_line(line_number: int) -> tuple[int, list[int]]:
    try:
        line = input().split()
    except EOFError as e:
        raise ParseError(f"unexpected end of input at line {line_number}") from e

    if not line:
        raise ParseError(f"line {line_number} is empty")

    try:
        numbers = list(map(int, line))
    except ValueError as e:
        raise ParseError(f"line {line_number} contains non-integer values") from e

    vertex = numbers[0]
    neighbors = numbers[1:]

    return vertex, neighbors


def parse_graph(n: int) -> dict[int, list[int]]:
    graph = {}

    for i in range(n):
        line_number = i + 1
        vertex, neighbors = parse_adjacency_line(line_number)

        if vertex in graph:
            raise ParseError(f"duplicate vertex {vertex}")

        graph[vertex] = neighbors

    return graph


def main():
    try:
        n = parse_args()
        graph = parse_graph(n)
        print("YES" if has_cycle(graph) else "NO")

    except ParseError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    except KeyboardInterrupt:
        sys.exit(130)


if __name__ == "__main__":
    main()

