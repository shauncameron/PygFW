from _thread import start_new_thread
from time import sleep
from sys import stdout

def when_is(object, value, do,do_args=(), check_interval_ms=10, **kwargs):
    
    def check_equals():
        
        while object is not value:
            
            sleep(check_interval_ms)
            pass

        do(*do_args)

    start_new_thread(check_equals, ())


def when_is_not(object, value, do,do_args=(), check_interval_ms=10, **kwargs):
    
    def check_equals():
        
        while object is value:
            
            sleep(check_interval_ms)
            pass

        do(*do_args)

    start_new_thread(check_equals, ())

def when_equals(object, value, do,do_args=(), check_interval_ms=10, **kwargs):
    
    def check_equals():
        
        while object != value:
            
            sleep(check_interval_ms)    
            pass
        
        do(*do_args)
        
    start_new_thread(check_equals, ())


def when_not_equals(object, value, do,do_args=(), check_interval_ms=10):
    
    def check_equals():

        while object == value:

            sleep(check_interval_ms)
            pass

        do(*do_args)

    start_new_thread(check_equals, ())


def when_returns(function, *function_args, value, do,do_args=(), check_interval_ms=10):

    def check_equals():

        while function(*function_args) != value:

            sleep(check_interval_ms)
            pass

        do(*do_args)

    start_new_thread(check_equals, ())


def when_not_returns(function, *function_args, value, do,do_args=(), check_interval_ms=10):

    def check_equals():

        while function(*function_args) != value:

            sleep(check_interval_ms)
            pass

        do(*do_args)

    start_new_thread(check_equals, ())