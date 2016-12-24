my assert
=========

*Simple python assertion library with verbose output.*

.. list-table::
    :stub-columns: 1

    * - tests
      - |travis| |coverage|
    * - package
      - |version|

.. |travis| image:: https://travis-ci.org/thaffenden/myassert.svg?branch=master
   :alt: Travis CI Build Status
   :target: https://travis-ci.org/thaffenden/myassert

.. |coverage| image:: https://coveralls.io/repos/github/thaffenden/myassert/badge.svg?branch=master
   :alt: Code Coverage
   :target: https://coveralls.io/github/thaffenden/myassert?branch=master

.. |version| image:: https://badge.fury.io/py/my-assert.svg
   :alt: Pypi Version
   :target: https://pypi.python.org/pypi/my-assert


**my assert** is a simple assertion library designed to give your assertion statements a more user friendly output.

It currently accommodates two main implementations:


Inheriting from the `AllAssertions` class
-----------------------------------------

You can superclass the *AllAssertions* class to provide direct access to the assertion statements through self.

.. code-block:: python

   from myassert import AllAssertions

   class MyNewClass(AllAssertions):

       def my_function(foo, bar):
           self.assert_equal(foo, bar)


All methods inside *AllAssertions* are static, so it requires no initialisation.



Importing the function directly
-------------------------------

You can also import the functions directly:

.. code-block:: python

   from myassert.assertions import assert_equal

   def my_function(foo, bar):
       assert_equal(foo, bar)
