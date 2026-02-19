# This file is part of the materials accompanying the book
# "Mathematical Logic through Python" by Gonczarowski and Nisan,
# Cambridge University Press. Book site: www.LogicThruPython.org
# (c) Yannai A. Gonczarowski and Noam Nisan, 2017-2022
# File name: propositions/operators.py

"""Syntactic conversion of propositional formulas to use only specific sets of
operators."""

from propositions.syntax import *
from propositions.semantics import *

def to_not_and_or(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'~'``, ``'&'``, and ``'|'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'~'``, ``'&'``, and
        ``'|'``.
    """
    base_var = next(iter(formula.variables()), 'p')

    def rewrite(node: Formula) -> Formula:
        if is_variable(node.root):
            return node

        if is_constant(node.root):
            v = Formula(base_var)
            nv = Formula('~', v)
            return Formula('|', v, nv) if node.root == 'T' else Formula('&', v, nv)

        if is_unary(node.root):
            return Formula('~', rewrite(node.first))

        a = rewrite(node.first)
        b = rewrite(node.second)

        if node.root == '&' or node.root == '|':
            return Formula(node.root, a, b)

        if node.root == '->':
            return Formula('|', Formula('~', a), b)

        if node.root == '+':
            return Formula('|',
                           Formula('&', a, Formula('~', b)),
                           Formula('&', Formula('~', a), b))

        if node.root == '<->':
            return Formula('|',
                           Formula('&', a, b),
                           Formula('&', Formula('~', a), Formula('~', b)))

        if node.root == '-&':
            return Formula('~', Formula('&', a, b))

        assert node.root == '-|'
        return Formula('~', Formula('|', a, b))

    return rewrite(formula)
    # Task 3.5

def to_not_and(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'~'`` and ``'&'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'~'`` and ``'&'``.
    """
    # Task 3.6a

def to_nand(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'-&'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'-&'``.
    """
    # Task 3.6b

def to_implies_not(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'->'`` and ``'~'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'->'`` and ``'~'``.
    """
    # Task 3.6c

def to_implies_false(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'->'`` and ``'F'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'->'`` and ``'F'``.
    """
    # Task 3.6d
