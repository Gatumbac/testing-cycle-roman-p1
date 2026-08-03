# TESTING CYCLE

Gabriel Tumbaco Santana

## Part 2

![](./img/img1.png)

## Part 3

### 9. Control flow graph of `to_roman`

![](./img/img2.png)

| Node | Line | Statement |
|---|---|---|
| 1 | 40 | `def to_roman(n):` |
| 2 | 41 | `if not isinstance(n, int) or isinstance(n, bool):` |
| 3 | 42 | `raise RomanError("value must be an integer")` |
| 4 | 43 | `if n < _MIN_VALUE:` |
| 5 | 44 | `raise RomanError("value must be >= 1")` |
| 6 | 45 | `if n > _MAX_VALUE:` |
| 7 | 46 | `raise RomanError("value must be <= 3999")` |
| 8 | 47 | `out = []` |
| 9 | 48 | `remaining = n` |
| 10 | 49 | `for value, symbol in _PAIRS:` |
| 11 | 50 | `while remaining >= value:` |
| 12 | 51 | `out.append(symbol)` |
| 13 | 52 | `remaining -= value` |
| 14 | 53 | `return "".join(out)` |

Edges (18): 1→2, 2→3, 2→4, 3→14, 4→5, 4→6, 5→14, 6→7, 6→8, 7→14, 8→9, 9→10,
10→11, 10→14, 11→12, 11→10, 12→13, 13→11.

### 10. Cyclomatic complexity

```
E = 18
N = 14

V(G) = E - N + 2
V(G) = 18 - 14 + 2
V(G) = 6
```

Predicates at nodes 2, 4, 6, 10, 11 → 5 + 1 = 6.

### 11. Basis set

| # | Path | Input | Expected |
|---|---|---|---|
| P1 | 1, 2, 3, 14 | `to_roman("5")` | `RomanError` "value must be an integer" |
| P2 | 1, 2, 4, 5, 14 | `to_roman(0)` | `RomanError` "value must be >= 1" |
| P3 | 1, 2, 4, 6, 7, 14 | `to_roman(4000)` | `RomanError` "value must be <= 3999" |
| P4 | 1, 2, 4, 6, 8, 9, 10, 14 | infeasible: `_PAIRS` is never empty | `""` |
| P5 | 1, 2, 4, 6, 8, 9, 10, 11, 10, 14 | `to_roman(1)` | `"I"` |
| P6 | 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 11, 10, 14 | `to_roman(1000)` | `"M"` |

P5 and P6 cover the edges of P4 (6→8, 8→9, 9→10, 10→14), so every edge is executed.

### 12. Definition-use table

| Variable | def | use | Kind | Pair | Def-clear path |
|---|---|---|---|---|---|
| `n` | 1 | 2 | p-use | (1, 2) | 1-2 |
| `n` | 1 | 4 | p-use | (1, 4) | 1-2-4 |
| `n` | 1 | 6 | p-use | (1, 6) | 1-2-4-6 |
| `n` | 1 | 9 | c-use | (1, 9) | 1-2-4-6-8-9 |
| `out` | 8 | 12 | c-use | (8, 12) | 8-9-10-11-12 |
| `out` | 8 | 14 | c-use | (8, 14) | 8-9-10-14 |
| `remaining` | 9 | 11 | p-use | (9, 11) | 9-10-11 |
| `remaining` | 9 | 13 | c-use | (9, 13) | 9-10-11-12-13 |
| `remaining` | 13 | 11 | p-use | (13, 11) | 13-11 |
| `remaining` | 13 | 13 | c-use | (13, 13) | 13-11-12-13 |
| `value` | 10 | 11 | p-use | (10, 11) | 10-11 |
| `value` | 10 | 13 | c-use | (10, 13) | 10-11-12-13 |
| `symbol` | 10 | 12 | c-use | (10, 12) | 10-11-12 |
| `_PAIRS` | module, 5 | 10 | c-use | (5, 10) | reaches 10 |
| `_MIN_VALUE` | module, 36 | 4 | p-use | (36, 4) | reaches 4 |
| `_MAX_VALUE` | module, 37 | 6 | p-use | (37, 6) | reaches 6 |

Pairs from the redefinition inside the loop: `remaining -= value` at node 13 is a c-use and
a def, so it opens (13, 11) and (13, 13) and kills the def at node 9. (9, 11) requires an
input whose first pair is skipped (`to_roman(1)`); (13, 11) and (13, 13) require two or more
passes through the body (`to_roman(2000)`). `value` and `symbol` are redefined at node 10 on
each iteration, so their pairs never cross iterations.

### 13. Branch coverage

```
pytest --cov=roman.converter --cov-branch --cov-report=term-missing
```

## Part 4

## Part 5

## Part 6

## Coverage
