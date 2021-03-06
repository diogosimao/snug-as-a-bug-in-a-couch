SnugAsABugInACouch
=====================================================

yet another watchlist manager

[![Build Status](https://travis-ci.org/diogosimao/snug-as-a-bug-in-a-couch.svg?branch=master)](https://travis-ci.org/diogosimao/snug-as-a-bug-in-a-couch)
[![Coverage Status](https://coveralls.io/repos/github/diogosimao/snug-as-a-bug-in-a-couch/badge.svg?branch=master)](https://coveralls.io/github/diogosimao/snug-as-a-bug-in-a-couch?branch=master)
[![Code Health](https://landscape.io/github/diogosimao/snug-as-a-bug-in-a-couch/master/landscape.svg?style=flat)](https://landscape.io/github/diogosimao/snug-as-a-bug-in-a-couch/master)
[![Requirements Status](https://requires.io/github/diogosimao/snug-as-a-bug-in-a-couch/requirements.svg?branch=master)](https://requires.io/github/diogosimao/snug-as-a-bug-in-a-couch/requirements/?branch=master)

Stack
=============

* pipenv
* pip
* Python 3.6

Info
====

There are two options to setup and run the app. You can either choose to setup the Docker (ToDo) environment or run it via `pipenv` (virtualenv like system). In both options you must have the 'stack' installed. 

Docker setup requirements 
=============================

* Docker CE (lastest) installed
    * Installation
        * Docker, see [here](https://docs.docker.com/installation/)
    
    * Used Docker images:
        * Python 3.6
        * Postgres
        * Nginx

Run the app
===========

1. Git clone this [repo](https://github.com/diogosimao/snug-as-a-bug-in-a-couch.git). 
    
    $ git clone https://github.com/diogosimao/snugasabuginacouch.git && cd snugasabuginacouch

2. Make sure you have `pipenv` installed via `pip`.

3. Use `pipenv` to create a virtualenv, install its dependencies and activate the virtualenv.

    $ pipenv --three && pipenv shell

4. Run `. ./bin/start_development.sh`


#### Note: lookup `./bin` directory  in order to get more options so that you can run the app.  


Hosted on Heroku
================

[Link](http://snugasabuginacouch.herokuapp.com/)

Acknowledgments
=============
[Leon Revill](https://blog.revillweb.com/bootstrap-tutorial-a-responsive-design-tutorial-with-twitter-bootstrap-3-cb6445c1e586)
