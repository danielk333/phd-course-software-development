---
title: "Styles of development"
lecture: "07-development"
weight: 7
---

## Development Styles

There are many different styles of development, e.g.

- [Iterative design](https://en.wikipedia.org/wiki/Iterative_design)
- [Iterative and incremental development](https://en.wikipedia.org/wiki/Iterative_and_incremental_development)
- [Test-driven development](https://en.wikipedia.org/wiki/Test-driven_development)
- [V](https://en.wikipedia.org/wiki/V-model_(software_development))
- [Software prototyping](https://en.wikipedia.org/wiki/Software_prototyping)
- [Continuous deployment](https://en.wikipedia.org/wiki/Continuous_deployment) or [Continuous delivery](https://en.wikipedia.org/wiki/Continuous_delivery)
- [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))
- [Waterfall](https://en.wikipedia.org/wiki/Waterfall_model)
- [Agile](https://en.wikipedia.org/wiki/Agile_software_development)
- [Lean](https://en.wikipedia.org/wiki/Lean_software_development) &
[Kanban](https://en.wikipedia.org/wiki/Kanban)
- And probably a bunch more

Although, for us scientists I believe really only a select few are relevant, which are also the ones covered
in the lecture.

A few brief explanations of relevant styles can be found in the videos below since the articles
above can be quite long and wordy.

TheAgileBroadcast - Is agile incremental or iterative?
{{< youtube 20SdEYJEbrE >}}


ProDeveloper - Software Development Methodologies Introduction
{{< youtube WSq72fWYLDE >}}

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

If you want to use advanced `pytest` features, you can read more about them [here](https://docs.pytest.org/en/7.1.x/how-to/parametrize.html). For testing of `numpy` arrays I recommend using the built in [test support](https://numpy.org/doc/stable/reference/routines.testing.html). To read more about what kind of assert helper `unittest` provides, see the [TestCase docs](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug). A particularly useful helper is for testing that functions fail as expected using e.g. `assertRaises` as in

```python
with self.assertRaises(SomeException):
    do_something()
```

Reflection afterwards
: Did you anticipate all the aspects you needed to test? What was missing? Where there useless
: tests? Why? Would it have been easier or harder to start without tests?

