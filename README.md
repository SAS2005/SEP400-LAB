# SEP400 Lab — Testing, Coverage, Static Analysis and TDD

This repository contains the completed SEP400 Software Engineering lab exercises focused on software testing and code quality in Python.

## Lab objectives

The lab covers three main areas:

1. **Unit testing** with Python's `unittest` framework
2. **Code coverage** using `coverage.py`, including line and branch coverage
3. **Static analysis** using `pylint`
4. **Test Driven Development (TDD)** using the Red → Green → Refactor workflow

## Task 1 — Unit Testing and Coverage

The program `rövarspråket.py` translates normal text into Rövarspråket.

A separate test file, `tests.py`, was created using `unittest`. The tests were used to detect and correct bugs in the original implementation, including incorrect handling of the Swedish vowels **O/o** and **Ö/ö**.

Final result:

- 9 unit tests passing
- 100% line coverage
- 100% branch coverage

Run the tests:

```bash
python3 tests.py
```

Run coverage:

```bash
python3 -m coverage erase
python3 -m coverage run --branch --source=rövarspråket tests.py
python3 -m coverage report -m
```

Generate the HTML coverage report:

```bash
python3 -m coverage html
open htmlcov/index.html
```

## Task 2 — Static Analysis with Pylint

`pylint` was used to analyze and improve `rövarspråket.py` without changing its behavior.

The original code contained issues such as:

- unused imports
- missing function docstrings
- inconsistent variable naming
- unnecessary `elif` statements after `return`
- too many return statements

After refactoring, all unit tests still passed and the final Pylint score was:

```text
10.00 / 10
```

Run Pylint:

```bash
python3 -m pylint rövarspråket.py
```

## Task 3 — Test Driven Development

The function `moms(p, tax)` was implemented using TDD. Each requirement was developed by first writing a failing test, then adding the minimum implementation needed to make the test pass.

The implemented requirements are:

- `p >= 0` → return the price including VAT
- `p < 0` → use the absolute value of the price
- `p > 1_000_000` → raise `ValueError("Absurdly high price")`
- `tax <= 0` → raise `ValueError("Illegal tax")`
- `tax > 100` → raise `ValueError("Illegal tax")`

Final result:

- 5 TDD tests passing

Run the TDD tests:

```bash
python3 test_moms.py
```

## Project structure

```text
SEP400-LAB/
├── rövarspråket.py   # Rövarspråket implementation
├── tests.py          # Unit tests for rövarspråket.py
├── moms.py           # VAT function developed with TDD
├── test_moms.py      # Tests for moms.py
├── .gitignore
└── README.md
```

## Tools used

- Python 3
- `unittest`
- `coverage.py`
- `pylint`
- Git and GitHub

## Final verification

```text
rövarspråket tests: 9/9 passed
moms tests:         5/5 passed
Pylint:             10.00/10
Line coverage:      100%
Branch coverage:    100%
```
