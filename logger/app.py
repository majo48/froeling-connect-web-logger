""" top-level logger app
    Copyright (c) 2020 M. Jonasse (martin.jonasse@mail.ch)
    functions:
        run(username, password, period_minutes)

"""
import sys
from logger import session
from logger import scheduler


def run(username=None, password=None, period_minutes=None):
    """ argument == 'None' will be replaced with the value from the configuration file """
    try:
        from logger import local_settings
        if username == None:
            username = local_settings.username()
        if password == None:
            password = local_settings.password()
        if period_minutes == None:
            period_minutes = local_settings.period_minutes()
        # run the internet query for the first time
        start_session = session.Session(local_settings.login_url(), username, password)
        # repeat the intenet query at fixed times (schedule)
        start_schedule = scheduler.Scheduler(username, password, period_minutes)
        # run until process (thread) is killed by user
    #
    except ModuleNotFoundError:
        print('ModuleNotFoundError: please copy local_settings.py.dist to local_settings.py')


def manage_arguments():
    """ handle functional arguments from command line interface """
    arg_cnt = len(sys.argv)
    if arg_cnt == 1:
        # no arguments
        run()
    elif arg_cnt == 2:
        # first argument
        run(sys.argv[1])
    elif arg_cnt == 3:
        # two arguments
        run(sys.argv[1], sys.argv[2])
    elif arg_cnt == 4:
        # three arguments
        run(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print('Error: too many arguments')


if __name__ == '__main__':
    manage_arguments()