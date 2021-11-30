from pyddl import Problem
from planner import planner
from one_passenger import create_domain_one_passenger
from multiple_passengers import create_domain_multiple_passengers


def problem_one_passenger(verbose, domain):
    problem = Problem(
        domain, objects={
            'taxi': ('T'),
            'passenger': ('P1', 'P2', 'P3'),
            'position': (1, 2, 3, 4, 5),
        },
        init=(  # The following are the predicates that you should use to define the operators above
            ('inc', 1, 2),
            ('inc', 2, 3),
            ('inc', 3, 4),
            ('inc', 4, 5),
            ('dec', 2, 1),
            ('dec', 3, 2),
            ('dec', 4, 3),
            ('dec', 5, 4),
            ('at', 'T', 1, 1),
            ('at', 'P1', 1, 2),
            ('at', 'P2', 1, 3),
            ('at', 'P3', 3, 3),
            ('free', 'T'),  # it means that taxi T is free
        ),
        goal=(  # Final states of each passenger (required locations)
            ('at', 'P1', 3, 4),
            ('at', 'P2', 3, 3),
            ('at', 'P3', 4, 3),
        )
    )
    print('----- Solving problem 1 -----')
    plan = planner(problem, verbose=verbose, heuristic=None)
    if plan is None:
        print('No Plan for planner 1 (one passenger)!')
    else:
        print("Successfully created a plan for problem 1 (one passenger)")
        for action in plan:
            print(action)


def problem_multiple_passengers(verbose, domain):
    problem = Problem(domain,
                      {
                          'taxi': ('T'),
                          'passenger': ('P1', 'P2', 'P3'),
                          'position': (1, 2, 3, 4, 5),
                      },
                      init=(  # The following are the predicates that you should use to define the operators above
                          ('inc', 1, 2),
                          ('inc', 2, 3),
                          ('inc', 3, 4),
                          ('inc', 4, 5),
                          ('dec', 2, 1),
                          ('dec', 3, 2),
                          ('dec', 4, 3),
                          ('dec', 5, 4),
                          ('at', 'T', 1, 1),
                          ('at', 'P1', 1, 2),
                          ('at', 'P2', 1, 3),
                          ('at', 'P3', 3, 3),
                          ('free', 'T'),  # it means that taxi (1) is free
                      ),
                      goal=(  # Final states of each passenger (required locations)
                          ('at', 'P1', 3, 4),
                          ('at', 'P2', 3, 3),
                          ('at', 'P3', 4, 3),
                      )
                      )
    print('----- Solving problem 2 -----')
    plan = planner(problem, verbose=verbose)
    if plan is None:
        print('No Plan for planner 2 (multiple passengers)!')
    else:
        print("Successfully created a plan for problem 2 (multiple passengers)")
        for action in plan:
            print(action)


if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser(usage="Usage: %prog [options]")
    parser.add_option('-q', '--quiet',
                      action='store_false', dest='verbose', default=True,
                      help="don't print statistics to stdout")

    # Parse arguments
    opts, args = parser.parse_args()
    #domain = create_domain_one_passenger()
    #problem_one_passenger(opts.verbose, domain)

    domain = create_domain_multiple_passengers()
    problem_multiple_passengers(opts.verbose, domain)

