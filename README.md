# Hockey Exercises
## What?
A Python project, using Python3.12 and FastAPI, which will maintain a bunch of
media and exercises for use by individual hockey players at home. These will be
in a format similar ot many workout apps, and will allow the user (or player) to
work on their skills off the field, and outside of coaching time.

## Why?
It seems like a fun idea, and it allows me to sit and work through a bunch of
stuff to get to know the newer python ecosystem. This is one part learning, one
part playing, one part building. 

## Build & Test
Because this is a "learn the frameworks" project, obviously it uses a build tool
and a test framework. Tests are written with `pytest` and are run using `hatch`.
To ensure all dependencies are in place, make sure you have a `venv` set up and
activated, then run `pip install ./` from the root. This will pull in all the
dependencies you need. To run the tests, you can then run `hatch test` and any
other appropriate commands as usual.
