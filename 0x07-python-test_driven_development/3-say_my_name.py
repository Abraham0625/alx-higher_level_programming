0x07-python-test_driven_development


++++++++++++++++++++++++++++++++++++

++++++++++++++++++++++++++++++++++++

NOTE: CREATE THESE FIRST SET INSIDE THE /test/ DIRECTORY

++++++++++++++++++++++++++++++++++++

++++++++++++++++++++++++++++++++++++



0-add_integer.txt


# 0-add_integer.txt


===========================

How to Use 0-add_integer.py

===========================


This module defines an integer addition function ``add_integer(a, b=98)``.


Usage

=====


``add_integer(...)``` returns the addition of its two arguments. For numbers,

that value is equivalent to using the ``+`` operator.


::


    >>> add_integer = __import__('0-add_integer').add_integer

    >>> add_integer(2, 3)

    5


::


    >>> add_integer(2, -3)

    -1


The function also works with floating-point values.


::


    >>> add_integer(2.0, 3.0)

    5


Note that floats are casted to ints before addition is performed.


::


    >>> add_integer(2.9, 0.2)

    2


::


    >>> add_integer(-2.9, -0.2)

    -2


Floating and non-floating point values can be combined.


::


    >>> add_integer(2.3, -3)

    -1


The second argument is optional - by default, it is 98.


::


    >>> add_integer(2)

    100


Non-Numbers

===========


``add_integer()`` expects that both arguments are either integers or floats.

If either argument is a non-integer and non-float, a TypeError is raised:


::


    >>> add_integer("hello", 3)

    Traceback (most recent call last):

    TypeError: a must be an integer


::


    >>> add_integer(2, "hello")

    Traceback (most recent call last):

    TypeError: b must be an integer


::


    >>> add_integer(None)

    Traceback (most recent call last):

    TypeError: a must be an integer


::


    >>> add_integer(2.3, None)

    Traceback (most recent call last):

    TypeError: b must be an integer


If both arguments are non-integers and non-floats, a TypeError message is only

printed for the first argument.


::


    >>> add_integer("hello", "there")

    Traceback (most recent call last):

    TypeError: a must be an integer


The function will fail if infinity is provided.


::


    >>> add_integer(float('inf'))

    Traceback (most recent call last):

    OverflowError: cannot convert float infinity to integer

     


::


    >>> add_integer(2, float('inf'))

    Traceback (most recent call last):

    OverflowError: cannot convert float infinity to integer


And again with NaN numbers.


::


    >>> add_integer(float('nan'))

    Traceback (most recent call last):

    ValueError: cannot convert float NaN to integer


::


    >>> add_integer(2, float('nan'))

    Traceback (most recent call last):

    ValueError: cannot convert float NaN to integer



++++++++++++++++++++++++++++++++++


2-matrix_divided.txt


# 2-matrix_divided.txt


==============================

How to Use 2-matrix_divided.py

==============================


This module defines a matrix division function ``matrix_divided(matrix, div)``.


Usage

=====


``matrix_divided(...)`` returns a new matrix that is a copy of the parameter

``matrix`` with all elements divided by ``div``.


::


    >>> matrix_divided = __import__('2-matrix_divided').matrix_divided

    >>> matrix = [

    ...     [3, 6, 9],

    ...     [12, 15, 18]

    ... ]

    >>> print(matrix_divided(matrix, 3))

    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]


Note that quotients are rounded to a maximum of two decimal places.


::


    >>> matrix = [

    ...     [1, 2, 3],

    ...     [4, 5, 6]

    ... ]

    >>> print(matrix_divided(matrix, 3))

    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]


The original matrix is left unchanged.


::


    >>> print(matrix)

    [[1, 2, 3], [4, 5, 6]]


The function can also handle floating-point numbers.


::


    >>> matrix = [

    ...     [1.1, -2.2, 3.3],

    ...     [4.4, 5.5, -6.6]

    ... ]

    >>> print(matrix_divided(matrix, 3))

    [[0.37, -0.73, 1.1], [1.47, 1.83, -2.2]]


Integers and floats can be combined.


::


    >>> matrix = [

    ...     [1, -2.2, 3, 4.4, 5],

    ...     [-6.6, 7.00, 8, 9.999, 10]

    ... ]

    >>> print(matrix_divided(matrix, 3))

    [[0.33, -0.73, 1.0, 1.47, 1.67], [-2.2, 2.33, 2.67, 3.33, 3.33]]


Invalid Matrices

==============


The parameter ``matrix`` must be a list of lists consisting of either ints or

floats. If ``matrix`` is not a list, a TypeError is raised.


::


    >>> matrix = "not a list"

    >>> print(matrix_divided(matrix, 3))

    Traceback (most recent call last):

    TypeError: matrix must be a matrix (list of lists) of integers/floats


::


    >>> matrix = None

    >>> print(matrix_divided(matrix, 3))

    Traceback (most recent call last):

    TypeError: matrix must be a matrix (list of lists) of integers/floats


Note that an empty list will raise the TypeError.


::


    >>> matrix = []

    >>> print(matrix_divided(matrix, 3))

    Traceback (most recent call last):

    TypeError: matrix must be a matrix (list of lists) of integers/floats


But an empty list of lists will succeed.


::


    >>> matrix = [[]]

    >>> print(matrix_divided(matrix, 3))

    [[]]


An identical TypeError is raised if ``matrix`` is not specifically a list of

lists.


::


    >>> matrix = [1, 2, 3]

    >>> print(matrix_divided(matrix, 3))

    Traceback (most recent call last):

    TypeError: matrix must be a matrix (list of lists) of integers/floats


The same TypeError is raised yet again if any elements in ``matrix`` are

neither ints nor floats.


::


    >>> matrix = [

    ...     [1, 2, 3],

    ...     [4, "not a number", 6]

    ... ]

    >>> print(matrix_divided(matrix, 3))

    Traceback (most recent call last):

    TypeError: matrix must be a matrix (list of lists) of integers/floats



Finally, all the rows in ``matrix`` must be the same size. If any rows are

of different sizes, a new TypeError is raised.


::


    >>> matrix = [

    ...     [1, 2, 3, 4],

    ...     [5, 6, 7]

    ... ]

    >>> print(matrix_divided(matrix, 3))

    Traceback (most recent call last):

    TypeError: Each row of the matrix must have the same size


Invalid Divisors

================


The parameter ``div`` must be either an int or float. Otherwise, a TypeError

is raised.


::


    >>> matrix = [

    ...     [1, 2, 3],

    ...     [4, 5, 6]

    ... ]

    >>> print(matrix_divided(matrix, "not a number"))

    Traceback (most recent call last):

    TypeError: div must be a number


::


    >>> print(matrix_divided(matrix, None))

    Traceback (most recent call last):

    TypeError: div must be a number


``div`` must also be non-zero. Otherwise, a ZeroDivisionError is raised.


::


    >>> print(matrix_divided(matrix, 0))

    Traceback (most recent call last):

    ZeroDivisionError: division by zero



+++++++++++++++++++++++++++++++++++++


3-say_my_name.txt


# 3-say_my_name.txt


===========================

How to Use 3-say_my_name.py

===========================


This modules defines a function ``say_my_name(first_name, last_name="")``.


Usage

=====


``say_my_name(...)`` prints "My name is <first_name> <last_name>".


::


    >>> say_my_name = __import__('3-say_my_name').say_my_name

    >>> say_my_name("Brennan", "Baraban")

    My name is Brennan Baraban


::


    >>> say_my_name("Cornelius Maxwell", "Jones II")

    My name is Cornelius Maxwell Jones II


The parameter ```last_name``` is optional. If no last name is provided,

an empty string is printed instead.


::


    >>> say_my_name("Brennan")

    My name is Brennan


Invalid Names

=============


The parameters ``first_name`` and ``last_name``` must be strings. Otherwise,

a TypeError is raised.


::


    >>> say_my_name(6, "James")

    Traceback (most recent call last):

    TypeError: first_name must be a string


::


    >>> say_my_name("LeBron", ["Cavs", "Lakers", "Heat"])

    Traceback (most recent call last):

    TypeError: last_name must be a string


::


    >>> say_my_name({"LeBron": 6, "James": 23}, 7.7)

    Traceback (most recent call last):

    TypeError: first_name must be a string


::


    >>> say_my_name(None)

    Traceback (most recent call last):

    TypeError: first_name must be a string


At least one name must be provided.


::


    >>> say_my_name()

    Traceback (most recent call last):

    TypeError: say_my_name() missing 1 required positional argument: 'first_name'



+++++++++++++++++++++++++++++++++

4-print_square.txt


# 4-print_square.txt


============================

How to Use 4-print_square.py

============================


This module defines a square-printing function ``print_square(size)``.


Usage

=====


Squares are printed using the ``#`` character. The parameter ``size``

represents the height and width of the square.


::


    >>> print_square = __import__('4-print_square').print_square

    >>> print_square(1)

    #


::


    >>> print_square(4)

    ####

    ####

    ####

    ####


::


    >>> print_square(10)

    ##########

    ##########

    ##########

    ##########

    ##########

    ##########

    ##########

    ##########

    ##########

    ##########


If ``size`` is zero, the function prints nothing.


::


    >>> print_square(0)


Invalid Sizes

=============


The parameter ``size`` must be an integer. Otherwise, a TypeError is raised.


::


    >>> print_square("not an int")

    Traceback (most recent call last):

    TypeError: size must be an integer


::


    >>> print_square(5.5)

    Traceback (most recent call last):

    TypeError: size must be an integer


::


    >>> print_square(None)

    Traceback (most recent call last):

    TypeError: size must be an integer


If ``size`` is less than zero, a ValueError is raised.


::


    >>> print_square(-7)

    Traceback (most recent call last):

    ValueError: size must be >= 0


Note that type-checking occurs before value-checking.


::


    >>> print_square(-7.5)

    Traceback (most recent call last):

    TypeError: size must be an integer


At least one argument must be provided.


::


    >>> print_square()

    Traceback (most recent call last):

    TypeError: print_square() missing 1 required positional argument: 'size'



+++++++++++++++++++++++++++++++++


5-text_indentation.txt


# 5-text_indentation.txt


================================

How to Use 5-text_indentation.py

================================


This module defines a text-indentation function ``text_indentation(text)``.


Usage

=====


Text is printed with two new lines after each of the characters ``.``, ``?``,

and ``:``.


::


    >>> text_indentation = __import__('5-text_indentation').text_indentation

    >>> text_indentation("Hello?")

    Hello?

    <BLANKLINE>


No spaces are printed at the beginning of a line.


::


    >>> text_indentation("   Hi there.")

    Hi there.

    <BLANKLINE>


::


    >>> text_indentation("          ")


Similarly, no spaces are printed at the end of each printed line.


::


    >>> text_indentation("Hello.   ")

    Hello.

    <BLANKLINE>


::


    >>> text_indentation("    Woah now.    This is messy.   ")

    Woah now.

    <BLANKLINE>

    This is messy.

    <BLANKLINE>


New lines are only printed for the characters ``.``, ``?``, and ``:`` -

text not ending with one of these characters is not ended with a new line.


::


    >>> text_indentation("No ending period, what bad grammar")

    No ending period, what bad grammar


New lines within a string are printed as normal.


::


    >>> text_indentation("Let's print a new-line! Here goes:\nPrinted.")

    Let's print a new-line! Here goes:

    <BLANKLINE>

    <BLANKLINE>

    Printed.

    <BLANKLINE>


::


    >>> text_indentation("\n\n\n We just printed three new lines.")

    <BLANKLINE>

    <BLANKLINE>

    <BLANKLINE>

    We just printed three new lines.

    <BLANKLINE>


::

    >>> text_indentation("A sneaky \n new line.")

    A sneaky

    new line.

    <BLANKLINE>


A combo example:


::


    >>> text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing "

    ... "elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas "

    ... "commovere? Non autem hoc: igitur ne illud quidem. Fortasse id optimum, "

    ... "sed ubi illud: Plus semper voluptatis? Teneo, inquit, finem illi videri "

    ... "nihil dolere. Transfer idem ad modestiam vel temperantiam, quae est "

    ... "moderatio cupiditatum rationi oboediens. Si id dicis, vicimus. Inde "

    ... "sermone vario sex illa a Dipylo stadia confecimus. Sin aliud quid "

    ... "voles, postea. Quae animi affectio suum cuique tribuens atque hanc, "

    ... "quam dico. Utinam quidem dicerent alium alio beatiorem! Iam ruinas "

    ... "videres") # doctest: +NORMALIZE_WHITESPACE

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.

    <BLANKLINE>

    Quonam modo?

    <BLANKLINE>

    Utrum igitur tibi litteram videor an totas paginas commovere?

    <BLANKLINE>

    Non autem hoc:

    <BLANKLINE>

    igitur ne illud quidem.

    <BLANKLINE>

    Fortasse id optimum, sed ubi illud:

    <BLANKLINE>

    Plus semper voluptatis?

    <BLANKLINE>

    Teneo, inquit, finem illi videri nihil dolere.

    <BLANKLINE>

    Transfer idem ad modestiam vel temperantiam,

    quae est moderatio cupiditatum rationi oboediens.

    <BLANKLINE>

    Si id dicis, vicimus.

    <BLANKLINE>

    Inde sermone vario sex illa a Dipylo stadia confecimus.

    <BLANKLINE>

    Sin aliud quid voles, postea.

    <BLANKLINE>

    Quae animi affectio suum cuique tribuens atque hanc, quam dico.

    <BLANKLINE>

    Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres


Invalid Text

============


The paramter ``text`` must be a string. Otherwise, a TypeError is raised.


::


    >>> text_indentation(7)

    Traceback (most recent call last):

    TypeError: text must be a string


::


    >>> text_indentation({"one": 1, "two": 2})

    Traceback (most recent call last):

    TypeError: text must be a string


::


    >>> text_indentation(None)

    Traceback (most recent call last):

    TypeError: text must be a string



++++++++++++++++++++++++++++++++


6-max_integer_test.py


#!/usr/bin/python3

# 6-max_integer_test.py

"""Unittests for max_integer([..])."""


import unittest

max_integer = __import__('6-max_integer').max_integer



class TestMaxInteger(unittest.TestCase):

    """Define unittests for max_integer([..])."""


    def test_ordered_list(self):

        """Test an ordered list of integers."""

        ordered = [1, 2, 3, 4]

        self.assertEqual(max_integer(ordered), 4)


    def test_unordered_list(self):

        """Test an unordered list of integers."""

        unordered = [1, 2, 4, 3]

        self.assertEqual(max_integer(unordered), 4)


    def test_max_at_begginning(self):

        """Test a list with a beginning max value."""

        max_at_beginning = [4, 3, 2, 1]

        self.assertEqual(max_integer(max_at_beginning), 4)


    def test_empty_list(self):

        """Test an empty list."""

        empty = []

        self.assertEqual(max_integer(empty), None)


    def test_one_element_list(self):

        """Test a list with a single element."""

        one_element = [7]

        self.assertEqual(max_integer(one_element), 7)


    def test_floats(self):

        """Test a list of floats."""

        floats = [1.53, 6.33, -9.123, 15.2, 6.0]

        self.assertEqual(max_integer(floats), 15.2)


    def test_ints_and_floats(self):

        """Test a list of ints and floats."""

        ints_and_floats = [1.53, 15.5, -9, 15, 6]

        self.assertEqual(max_integer(ints_and_floats), 15.5)


    def test_string(self):

        """Test a string."""

        string = "Brennan"

        self.assertEqual(max_integer(string), 'r')


    def test_list_of_strings(self):

        """Test a list of strings."""

        strings = ["Brennan", "is", "my", "name"]

        self.assertEqual(max_integer(strings), "name")


    def test_empty_string(self):

        """Test an empty string."""

        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':

    unittest.main()



+++++++++++++++++++++++++++++++++++


100-matrix_mul.txt


# 100-matrix_mul.txt


============================

How to Use 100-matrix_mul.py

============================


This module defines a matrix multiplication function ``matrix_mul(m_a, m_b)``.


Usage

=====

``matrix_mul(...)`` returns a new matrix representing the multiplication of

``m_a`` by ``m_b``.


::


    >>> matrix_mul = __import__('100-matrix_mul').matrix_mul

    >>> m_a = [

    ... [1, 2],

    ... [3, 4],

    ... ]

    >>> m_b = m_a

    >>> print(matrix_mul(m_a, m_b))

    [[7, 10], [15, 22]]


::


    >>> m_a = [[1, 2]]

    >>> m_b = [

    ... [3, 4],

    ... [5, 6]

    ... ]

    >>> print(matrix_mul(m_a, m_b))

    [[13, 16]]


The function also works with floating-point numbers.


::


    >>> m_a = [

    ... [1.2, 5.5, 6.2],

    ... [4.66, 12.3, -9.2]

    ... ]

    >>> m_b = [

    ... [5.0, 3.3],

    ... [-2.9, 4.4],

    ... [7.2, 4.4]

    ... ]

    >>> print(matrix_mul(m_a, m_b))

    [[34.69, 55.44000000000001], [-78.61, 29.018000000000008]]


Integers and floats can be combined.


::


    >>> m_a = [

    ... [1, 2.2, 3.3, 4],

    ... [5, 6, 7, 8.8],

    ... ]

    >>> m_b = [

    ... [1.1, 2, 3.3],

    ... [4.0, 5.5, 6],

    ... [7, 8, 9],

    ... [10.01, 11, 12.3]

    ... ]

    >>> print(matrix_mul(m_a, m_b))

    [[73.03999999999999, 84.5, 95.4], [166.58800000000002, 195.8, 223.74]]


A minimum of two arguments must be provided. Otherwise, a TypeError is raised.


::


    >>> print(matrix_mul()) # doctest: +NORMALIZE_WHITESPACE

    Traceback (most recent call last):

    TypeError: matrix_mul() missing 2 required positional arguments:

    'm_a' and 'm_b'


::


    >>> print(matrix_mul()) # doctest: +NORMALIZE_WHITESPACE

    Traceback (most recent call last):

    TypeError: matrix_mul() missing 2 required positional arguments:

    'm_a' and 'm_b'


ValueErrors

===========


If two matrices cannot be multiplied (ie. the row count of ``m_a`` is not

equal to the column count in ``m_b``), a ValueError is raised.


::


    >>> m_a = [

    ... [1, 2],

    ... [3, 4],

    ... ]

    >>> m_b = [

    ... [1, 2],

    ... [2, 3],

    ... [4, 5]

    ... ]

    >>> print(matrix_mul(m_a, m_b))

    Traceback (most recent call last):

    ValueError: m_a and m_b can't be multiplied



The parameters ``m_a`` and ``m_b`` cannot be empty. Otherwise, a ValueError

is raised.


::


    >>> print(matrix_mul([], [[1, 2]]))

    Traceback (most recent call last):

    ValueError: m_a can't be empty


::


    >>> print(matrix_mul([[1, 2]], [[]]))

    Traceback (most recent call last):

    ValueError: m_b can't be empty


::


    >>> print(matrix_mul([[]], []))

    Traceback (most recent call last):

    ValueError: m_a can't be empty


Invalid Matrices

================


The parameters ``m_a`` and ``m_b`` must be lists. If either parameter is

not a list, a TypeError is raised.


::


    >>> print(matrix_mul("not a list", [[1, 2]]))

    Traceback (most recent call last):

    TypeError: m_a must be a list


::


    >>> print(matrix_mul([[1, 2]], "also not a list"))

    Traceback (most recent call last):

    TypeError: m_b must be a list


::


    >>> print(matrix_mul("not a list", "also not a list"))

    Traceback (most recent call last):

    TypeError: m_a must be a list


::


    >>> print(matrix_mul(None, None))

    Traceback (most recent call last):

    TypeError: m_a must be a list


Not just any list - they *must* be lists of lists!


::


    >>> print(matrix_mul([1, 2], [[3, 4]]))

    Traceback (most recent call last):

    TypeError: m_a must be a list of lists


::


    >>> print(matrix_mul([[1, 2]], [3, 4]))

    Traceback (most recent call last):

    TypeError: m_b must be a list of lists


::


    >>> print(matrix_mul([1, 2], [3, 4]))

    Traceback (most recent call last):

    TypeError: m_a must be a list of lists


And not just any list of lists - they *must* be lists of lists containing

integers or floats!


::


    >>> print(matrix_mul([[1, "non-number"]], [[3, 4]]))

    Traceback (most recent call last):

    TypeError: m_a should contain only integers or floats


::


    >>> print(matrix_mul([[1, 2]], [[{"a": 1}, 8.8]]))

    Traceback (most recent call last):

    TypeError: m_b should contain only integers or floats


::


    >>> print(matrix_mul([[1, "non-number"]], [[{"a": 1}, 8.8]]))

    Traceback (most recent call last):

    TypeError: m_a should contain only integers or floats


Finally, the length of all rows in matrices ``m_a`` and ``m_b`` should be

equivalent. Otherwise, a TypeError is raised.


::


    >>> m_a = [

    ... [1, 2],

    ... [3, 4, 5]

    ... ]

    >>> m_b = [

    ... [1, 2],

    ... [3, 4]

    ... ]

    >>> print(matrix_mul(m_a, m_b))

    Traceback (most recent call last):

    TypeError: each row of m_a must should be of the same size


::


    >>> m_a = [

    ... [1, 2],

    ... [3, 4]

    ... ]

    >>> m_b = [

    ... [1, 2],

    ... [3, 4, 5]

    ... ]

    >>> print(matrix_mul(m_a, m_b))

    Traceback (most recent call last):

    TypeError: each row of m_b must should be of the same size


::


    >>> m_a = [

    ... [1, 2],

    ... [3, 4, 5]

    ... ]

    >>> m_b = m_a

    >>> print(matrix_mul(m_a, m_b))

    Traceback (most recent call last):

    TypeError: each row of m_a must should be of the same size



+++++++++++++++++++++++++++++++++++++++


101-lazy_matrix_mul.txt


# 101-lazy_matrix_mul.txt


=================================

How to Use 101-lazy_matrix_mul.py

=================================


This module defines a matrix multiplication function

``lazy_matrix_mul(m_a, m_b)``.


Usage

=====


``lazy_matrix_mul(...)`` returns a new matrix representing the multiplication

of ``m_a`` by ``m_b``.


::


    >>> lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

    >>> m_a = [

    ... [1, 2],

    ... [3, 4],

    ... ]

    >>> m_b = m_a

    >>> print(lazy_matrix_mul(m_a, m_b))

    [[ 7 10]

     [15 22]]


::


    >>> m_a = [[1, 2]]

    >>> m_b = [

    ... [3, 4],

    ... [5, 6]

    ... ]

    >>> print(lazy_matrix_mul(m_a, m_b))

    [[13 16]]


The function also works with floating-point numbers.


::


    >>> m_a = [

    ... [1.2, 5.5, 6.2],

    ... [4.66, 12.3, -9.2]

    ... ]

    >>> m_b = [

    ... [5.0, 3.3],

    ... [-2.9, 4.4],

    ... [7.2, 4.4]

    ... ]

    >>> print(lazy_matrix_mul(m_a, m_b))

    [[ 34.69   55.44 ]

     [-78.61   29.018]]


A minimum of two arguments must be provided.


::


    >>> print(lazy_matrix_mul(m_a))

    Traceback (most recent call last):

    TypeError: lazy_matrix_mul() missing 1 required positional argument: 'm_b'


::


    >>> print(lazy_matrix_mul()) # doctest: +NORMALIZE_WHITESPACE

    Traceback (most recent call last):

    TypeError: lazy_matrix_mul() missing 2 required positional arguments:

    'm_a' and 'm_b'


ValueErrors

===========


If two matrices cannot be multiplied (ie. the row count of ``m_a`` is not

equal to the column count in ``m_b``), a ValueError is raised.


::


    >>> m_a = [

    ... [1, 2],

    ... [3, 4],

    ... ]

    >>> m_b = [

    ... [1, 2],

    ... [2, 3],

    ... [4, 5]

    ... ]

    >>> print(lazy_matrix_mul(m_a, m_b))

    Traceback (most recent call last):

    ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)



The parameters ``m_a`` and ``m_b`` cannot be empty. Otherwise, a ValueError

is raised.


::


    >>> print(lazy_matrix_mul([[]], [[5, 6], [7, 8]]))

    Traceback (most recent call last):

    ValueError: shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)


::


    >>> print(lazy_matrix_mul([[5, 6], [7, 8]], [[]]))

    Traceback (most recent call last):

    ValueError: shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)


Invalid Matrices

================


The parameters ``m_a`` and ``m_b`` must be lists. If either parameter is

not a list, a ValueError is raised.


::


    >>> print(lazy_matrix_mul("not a list", [[1, 2]]))

    Traceback (most recent call last):

    ValueError: Scalar operands are not allowed, use '*' instead


::


    >>> print(lazy_matrix_mul([[1, 2]], "also not a list"))

    Traceback (most recent call last):

    ValueError: Scalar operands are not allowed, use '*' instead


::


    >>> print(lazy_matrix_mul("not a list", "also not a list"))

    Traceback (most recent call last):

    ValueError: Scalar operands are not allowed, use '*' instead


If either parameter is ``None``, a TypeError is raised.


::


    >>> print(lazy_matrix_mul(None, None))

    Traceback (most recent call last):

    TypeError: Object arrays are not currently supported


Not just any list - they *must* be lists of lists! Otherwise, behavior is

undefined.


::


    >>> print(lazy_matrix_mul([1, 2], [[3, 4]]))

    Traceback (most recent call last):

    ValueError: shapes (2,) and (1,2) not aligned: 2 (dim 0) != 1 (dim 0)


::


    >>> print(lazy_matrix_mul([[1, 2]], [3, 4]))

    [11]


::


    >>> print(lazy_matrix_mul([1, 2], [3, 4]))

    11


And not just any list of lists - they *must* be lists of lists containing

integers or floats! Otherwise, a ValueError or TypeError is raised


::


    >>> print(lazy_matrix_mul([[1, "non-number"]], [[3, 4]]))

    Traceback (most recent call last):

    ValueError: shapes (1,2) and (1,2) not aligned: 2 (dim 1) != 1 (dim 0)


::


    >>> print(lazy_matrix_mul([[5, 6], [7, 8]], [[5, "6"], [7, 8]]))

    Traceback (most recent call last):

    TypeError: invalid data type for einsum


::


    >>> print(lazy_matrix_mul([[1, "non-number"]], [[{"a": 1}, 8.8]]))

    Traceback (most recent call last):

    TypeError: Object arrays are not currently supported


Finally, the length of all rows in matrices ``m_a`` and ``m_b`` should be

equivalent. Otherwise, a ValueError is raised.


::


    >>> m_a = [

    ... [1, 2],

    ... [3, 4, 5]

    ... ]

    >>> m_b = [

    ... [1, 2],

    ... [3, 4]

    ... ]

    >>> print(lazy_matrix_mul(m_a, m_b))

    Traceback (most recent call last):

    ValueError: setting an array element with a sequence.


::


    >>> m_a = [

    ... [1, 2],

    ... [3, 4]

    ... ]

    >>> m_b = [

    ... [1, 2],

    ... [3, 4, 5]

    ... ]

    >>> print(lazy_matrix_mul(m_a, m_b))

    Traceback (most recent call last):

    ValueError: setting an array element with a sequence.


::


    >>> m_a = [

    ... [1, 2],

    ... [3, 4, 5]

    ... ]

    >>> m_b = m_a

    >>> print(lazy_matrix_mul(m_a, m_b))

    Traceback (most recent call last):

    ValueError: setting an array element with a sequence.



+++++++++++++++++++++++++++++++++++

+++++++++++++++++++++++++++++++++++

AFTER CREATING THE ABOVE FILES IN THE /test/ folder, GO AHEAD AND CREATE THE FILES BELOW DIRECTLY inside the 0x07-python-test_driven_development directory

+++++++++++++++++++++++++++++++++++

+++++++++++++++++++++++++++++++++++


README.md

# Python - Test-driven development


In this project, I started practicing test-driven development using `docstring`

and `unittest` in Python.


## Tests :heavy_check_mark:


* [tests](./tests): Folder of test files. Includes both Holberton-provided ones as well as the

following eight independently-developed:

  * [0-add_integer.txt](./tests/0-add_integer.txt)

  * [2-matrix_divided.txt](./tests/2-matrix_divided.txt)

  * [3-say_my_name.txt](./tests/3-say_my_name.txt)

  * [4-print_square.txt](./tests/4-print_square.txt)

  * [5-text_indentation.txt](./tests/text_indentation.txt)

  * [6-max_integer_test.py](./tests/6-max_integer_test.py)

  * [100-matrix_mul.txt](./tests/100-matrix_mul.txt)

  * [101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt)


## Function Prototypes :floppy_disk:


Prototypes for functions written in this project:


| File                     | Prototype                                    |

| ------------------------ | -------------------------------------------- |

| `0-add_integer.py`       | `def add_integer(a, b=98):`                  |

| `2-matrix_divided.py`    | `def matrix_divided(matrix, div):`           |

| `3-say_my_name.py`       | `def say_my_name(first_name, last_name=""):` |

| `4-print_square.py`      | `def print_square(size):`                    |

| `5-text_indentation.py`  | `def text_indentation(text):`                |

| `100-matrix_mul.py`      | `def matrix_mul(m_a, m_b):`                  |

| `101-lazy_matrix_mul.py` | `def lazy_matrix_mul(m_a, m_b):`             |

| `102-python.c`           | `void print_python_string(PyObject *p);`     |


## Tasks :page_with_curl:


* **0. Integers addition**

  * [0-add_integer.py](./0-add_integer.py): Python function that returns the integer addition

  of two numbers.

  * If either of `a` or `b` is not an `int` or `float`, a `TypeError` is raised

  with the message `a must be an integer` or `b must be an integer`.

  * If either of `a` or `b` is a `float`, it is casted to an `int`

  before addition.


* **1. Divide a matrix**

  * [2-matrix_divided.py](./2-matrix_divided.py): Python function that divides all

  elements of a matrix by a common divisor.

  * Returns a new matrix representing the division of all elements of `matrix`

  by `div`.

  * Quotients are rounded to two decimal places.

  * If `matrix` is not a list of lists of `int`s or `float`s, a `TypeError`

  is raised with the message `matrix must be a matrix (list of lists) of

  integers/floats`.

  * If `matrix` contains rows of different lengths, a `TypeError` is raised

  with the message `Each row of the matrix must have the same size`.

  * If the divisor `div` is not an `int` or `float`, a `TypeError` is raised

  with the message `div must be a number`.

  * If `div` is `0`, a `ZeroDivisionError` is raised with the message

  `division by zero`.


* **2. Say my name**

  * [3-say_my_name.py](./3-say_my_name.py): Python function that prints a name in

  the format `My name is <first_name> <last_name>`.

  * If either of `first_name` or `last_name` is not a `str`, a `TypeError` is

  raised with the message `first_name must be a string` or `last_name must be a

  string`.


* **3. Print square**

  * [4-print_square.py](./4-print_square.py): Python function that prints a square using

  the `#` character.

  * The paramter `size` represents the height/width of the square.

  * If `size` is not an `int`, a `TypeError` is raised  with the message,

  `size must be an integer`.

  * If `size` is less than `0`, a `ValueError` is raised with the message `size

  must be >= 0`.


* **4. Text indentation**

  * [5-text_indentation.py](./5-text_indentation.py): Python function that prints text with

  indentation.

  * Two new lines are printed after any `.`, `?`, or `:` character.

  * If `text` is not a `str`, a `TypeError` is raised with the message `text

  must be a string`.

  * No spaces are printed at the beginning or end of each printed line.


* **5. Max integer - Unittest**

  * [tests/6-max_integer_test.py](./tests/6-max_integer_text.py): Python class/script

  that runs unittests for the function `def max_integer(list=[]):`

  (provided by Holberton School).


* **6. Matrix multiplication**

  * [100-matrix_mul.py](./100-matrix_mul.py): Python function that multiplies two matrices.

  * Returns a new matrix representing the multiplication of `m_a` by `m_b`.

  * If either of `m_a` or `m_b` is empty (ie. `== []` or `== [[]]`), a

  `ValueError` is raised with the message `m_a can't be empty` or `m_b can't

  be empty`.

  * If either of `m_a` or `m_b` is not a list, a `TypeError` is raised with

  the message `m_a must be a list` or `m_b` must be a list.

  * If either of `m_a` or `m_b` is not a list of lists, a `TypeError` is raised

  with the message `m_a must be a list of lists` or `m_b must be a list of lists`.

  * If either of `m_a` or `m_b` is not a list of lists of `int`s or `float`s, a

  `TypeError` is raised with the message `m_a should contain only integers or

  floats` or `m_b should contain only integers or floats`.

  * If either of `m_a` or `m_b` contains rows of different lengths, a `TypeError`

  is raised with the message `each row of m_a must should be of the same size` or

  `each row of m_b must should be of the same size`.

  * If `m_a` and `m_b` cannot be multiplied (ie. row size of `m_a` does not match

  column size of `m_b`), a `ValueError` is raised with the message `m_a and m_b

  can't be multiplied`.


* **7. Lazy matrix multiplication**

  * [101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py): Python function that multiplies

  two matrices using the module `NumPy`.

  * Identical in function to [100-matrix_mul.py](./100-matrix_mul.py).


* **8. CPython #3: Python Strings**

  * [102-python.c](./102-python.c): C function that prints basic information about Python

  string objects.



++++++++++++++++++++++++++++++++++++++


0-main.py


#!/usr/bin/python3

add_integer = __import__('0-add_integer').add_integer


print(add_integer(1, 2))

print(add_integer(100, -2))

print(add_integer(2))

print(add_integer(100.3, -2))

try:

    print(add_integer(4, "School"))

except Exception as e:

    print(e)

try:

    print(add_integer(None))

except Exception as e:

    print(e)



++++++++++++++++++++++++++++++++++


2-main.py


#!/usr/bin/python3

matrix_divided = __import__('2-matrix_divided').matrix_divided


matrix = [

    [1, 2, 3],

    [4, 5, 6]

]

print(matrix_divided(matrix, 3))

print(matrix)



+++++++++++++++++++++++++++++++++++


3-main.py


#!/usr/bin/python3

say_my_name = __import__('3-say_my_name').say_my_name


say_my_name("John", "Smith")

say_my_name("Walter", "White")

say_my_name("Bob")

try:

    say_my_name(12, "White")

except Exception as e:

    print(e)



+++++++++++++++++++++++++++++++++++


4-main.py


#!/usr/bin/python3

print_square = __import__('4-print_square').print_square


print_square(4)

print("")

print_square(10)

print("")

print_square(0)

print("")

print_square(1)

print("")

try:

    print_square(-1)

except Exception as e:

    print(e)

print("")



+++++++++++++++++++++++++++++++


5-main.py


#!/usr/bin/python3

text_indentation = __import__('5-text_indentation').text_indentation


text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \

Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \

Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \

Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \

Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \

rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \

stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \

cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \

beatiorem! Iam ruinas videres""")



+++++++++++++++++++++++++++++++



0-add_integer.py


#!/usr/bin/python3

# 0-add_integer.py

"""Defines an integer addition function."""



def add_integer(a, b=98):

    """Return the integer addition of a and b.


    Float arguments are typecasted to ints before addition is performed.


    Raises:

        TypeError: If either of a or b is a non-integer and non-float.

    """

    if ((not isinstance(a, int) and not isinstance(a, float))):

        raise TypeError("a must be an integer")

    if ((not isinstance(b, int) and not isinstance(b, float))):

        raise TypeError("b must be an integer")

    return (int(a) + int(b))



========================


2-matrix_divided.py


#!/usr/bin/python3

# 2-matrix_divided.py

"""Defines a matrix division function."""



def matrix_divided(matrix, div):

    """Divide all elements of a matrix.


    Args:

        matrix (list): A list of lists of ints or floats.

        div (int/float): The divisor.

    Raises:

        TypeError: If the matrix contains non-numbers.

        TypeError: If the matrix contains rows of different sizes.

        TypeError: If div is not an int or float.

        ZeroDivisionError: If div is 0.

    Returns:

        A new matrix representing the result of the division.

    """

    if (not isinstance(matrix, list) or matrix == [] or

            not all(isinstance(row, list) for row in matrix) or

            not all((isinstance(ele, int) or isinstance(ele, float))

                    for ele in [num for row in matrix for num in row])):

        raise TypeError("matrix must be a matrix (list of lists) of "

                        "integers/floats")


    if not all(len(row) == len(matrix[0]) for row in matrix):

        raise TypeError("Each row of the matrix must have the same size")


    if not isinstance(div, int) and not isinstance(div, float):

        raise TypeError("div must be a number")


    if div == 0:

        raise ZeroDivisionError("division by zero")


    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])



===============================


3-say_my_name.py


#!/usr/bin/python3

# 3-say_my_name.py

"""Defines a name-printing function."""



def say_my_name(first_name, last_name=""):

    """Print a name.


    Args:

        first_name (str): The first name to print.

        last_name (str): The last name to print.

    Raises:

        TypeError: If either of first_name or last_name are not strings.

    """

    if not isinstance(first_name, str):

        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):

        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
