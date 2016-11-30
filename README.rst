my assert
=========

*Simple python assertion library with verbose output.*

.. image:: https://travis-ci.org/thaffenden/myassert.svg?branch=master
   :alt: Travis CI Build Status
   :target: https://travis-ci.org/thaffenden/myassert

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
