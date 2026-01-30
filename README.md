# cycle-detection

Detect cycles in directed graphs.

## Installation
```bash
git clone <...>
cd cycle-detection
rye sync
```

## CLI
```bash
$ rye run cycle-detection 3
1 2
2 3
3 1
YES
```
> help:
> ```
> rye run cycle-detection -h
> ```

Format: `VERTEX NEIGHBOR1 NEIGHBOR2 ...`

## API
```python
from cycle_detection import has_cycle

has_cycle({1: [2], 2: [3], 3: [1]})  # True (cycle)
has_cycle({1: [2], 2: [3], 3: []})   # False (no cycle)
has_cycle({1: [1]})                   # True (self-loop)
```

## Development
```bash
rye run pytest           # tests
rye run ruff check .     # lint
```

## License

MIT
