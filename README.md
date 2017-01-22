# Example project for testing uwsgi sharedmemory module

It's include 3 apps:
- flask_app_with_locks
- flask_app_without_locks
- lask_app_memoryview_with_locks

You can change application in uwsgi.ini

## Starting application
For start application simple run `make docker-start`


## Load testing

Change `load.ini` and run `make tank`.


## Compare result
Take data from 127.0.0.1:8051 and compare with logstring `[pid: 56|app: 0|req: 1499/6003]`.
