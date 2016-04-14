About
=====

A Vagrant virtual machine that installs all the needed software for a 
basic Computer Vision Bot.

Requirements
============

* VirtualBox 4.3.10
* Vagrant 1.6.2
* vagrant-proxyconf if you're gonna use a proxy

Getting started
===============

To initialize the virtual machine run the following command:

    $ vagrant up

The first time the virtual machine is started it will take some time to
install all the packages so be patient.

What You Get
============

An Ubuntu Trusty 64 VM with :

* Latest version of OpenCV with python bindings
* Numpy
* Scipy
* iPython
* SQLite
* Bottle
* Tesseract OCR with python bindings
* A REST stub interface in data/cv_bot

CV-BOT
======

Start the CV-BOT with the following commands from the guest
	$ cd /vagrant_data/data/cv_bot
	$ python server.py