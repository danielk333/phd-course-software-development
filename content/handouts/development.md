---
title: "Styles of development"
lecture: "07-development"
weight: 7
---


## Homework

### A calculator

Write a general purpose calculator that can parse any single line calculation with `*`, `+`, `-`,
and `/`. If it is too easy to do just `int`, also try to support `float` or even `complex`.

Develop this calculator using Test-driven development - write all the tests before you do a single
line on the actual calculator.

Use the following test template

```python
import unittest
import my_calculator

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(my_calculator.run("1 + 1"), 2)

    def test_sub(self):
        self.assertEqual(my_calculator.run("1 - 1"), 0)

if __name__ == "__main__":
    unittest.main()
```

Then, if you save the above as `tests.py` you can run the tests using 

```bash
python tests.py
```

or with `pytest` as

```bash
pytest tests.py
```

Reflection afterwards
: Did you anticipate all the aspects you needed to test? What was missing? Where there useless
: tests? Why? Would it have been easier or harder to start without tests?

