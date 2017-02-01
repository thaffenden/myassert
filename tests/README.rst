Tests, Tests, Tests
===================

Running Tests
-------------
This project uses pytest as the test runner.
In the root directory, just enter `pytest` and the tests should run.

Code Coverage
-------------
This project should always remain at 100% coverage, however due to the different data types possible to pass to these functions there may be items not full covered to the extent required.
For this reason we can't rely on the coverage alone as an indication of the comprehensiveness of testing.
Tests should cover at the very minimum: `int`, `str`, `list` and `dict` data types (additional data types will be added).

To get a code coverage report when running the tests you can use:
`pytest --cov-report term-missing --cov=myassert`
This will detail the percentage of code covered and highlight any lines not currently covered by the test.
