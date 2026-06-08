# Example Python Project

Test Python project with CI for agent-release testing.

## Installation

```bash
pip install -e .[dev]
```

## Usage

```python
from example import add, multiply

result = add(2, 3)
product = multiply(4, 5)
```

## Development

```bash
pytest tests/ -v
ruff check .
```

## Release

```bash
release 0.2.0
```
