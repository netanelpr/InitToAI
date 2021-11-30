from __future__ import print_function
from pyddl import Domain, Action, neg
from planner import planner

def create_domain_multiple_passengers():
    domain = Domain((
        Action(
            'move-up',  
            parameters=(
                ('taxi', 't'),
                ('position', 'px'),  # Current location on the x-axis
                ('position', 'py'),  # Current location on the y-axis
                ('position', 'by'),  # New location on the y-axis
            ),
            preconditions=(
                ('dec', 'py', 'by'),
                ('at', 't', 'px', 'py'),
            ),
            effects=(
                neg(('at', 't', 'px', 'py')),
                ('at', 't', 'px', 'by'),
            ),
        ),
        Action(
            'move-down',
            parameters=(
                ('taxi', 't'),
                ('position', 'px'),
                ('position', 'py'),
                ('position', 'by'),
            ),
            preconditions=(
                ('inc', 'py', 'by'),
                ('at', 't', 'px', 'py'),
            ),
            effects=(
                neg(('at', 't', 'px', 'py')),
                ('at', 't', 'px', 'by'),
            ),
        ),
        Action(
            'move-left',
            parameters=(
                ('taxi', 't'),
                ('position', 'px'),
                ('position', 'py'),
                ('position', 'bx'),
            ),
            preconditions=(
                ('dec', 'px', 'bx'),
                ('at', 't', 'px', 'py'),
            ),
            effects=(
                neg(('at', 't', 'px', 'py')),
                ('at', 't', 'bx', 'py'),
            ),
        ),
        Action(
            'move-right',
            parameters=(
                ('taxi', 't'),
                ('position', 'px'),
                ('position', 'py'),
                ('position', 'bx'),
            ),
            preconditions=(
                ('inc', 'px', 'bx'),
                ('at', 't', 'px', 'py'),
            ),
            effects=(
                neg(('at', 't', 'px', 'py')),
                ('at', 't', 'bx', 'py'),
            ),
        ),
        Action(
            'pick-up',
            parameters=(
                ('taxi', 't'),
                ('position', 'px'),
                ('position', 'py'),
                ('passenger', 'p'),
            ),
            preconditions=(
                ('at', 't', 'px', 'py'),
                ('at', 'p', 'px', 'py'),
            ),
            effects=(
                ('on_taxi', 'p'),
            ),
        ),
        Action(
            'put-down',
            parameters=(
                ('taxi', 't'),
                ('position', 'px'),
                ('position', 'py'),
                ('passenger', 'p'),
            ),
            preconditions=(
                ('at', 't', 'px', 'py'),
                ('on_taxi', 'p')
            ),
            effects=(
                neg(('on_taxi', 'p')),
                ('at', 'p', 'px', 'py'),
            ),
        ),
    ))
    return domain