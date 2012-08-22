Formhub
=======

.. image:: https://secure.travis-ci.org/modilabs/formhub.png?branch=master
  :target: http://travis-ci.org/modilabs/formhub

Installation
------------

Ubuntu 12.04
^^^^^^^^^^^^

Install system libraries and start services::

    # make sure your system is up to date
    sudo apt-get update

    # install system libraries
    sudo apt-get install default-jre gcc git mongodb python-dev python-pip python-numpy
    
    # clone formhub
    git clone git://github.com/modilabs/formhub.git
    
    # install the dependencies
    sudo pip install -r formhub/requirements.pip

    # create a database and start server:
    # for something other than sqlite, create a local-settings.py file
    python manage.py syncdb
    python manage.py migrate

    # start mongodb
    sudo service mongodb start
    # start formhub
    python manage.py runserver

You can browse the site at: http://localhost:8000/

.. note::

    If you are using a remote server, or need to access it via an intranet, do::

        python manage.py runserver 0.0.0.0:8000

    and navigate to: http://yourownaddress:8000/


(OPTIONAL) Apache and system administration tools:

    # apt-get install apache libapache2-mode-wsgi

    # apt-get install htop monit

    set up apache and monit

Ubuntu 10.04
^^^^^^^^^^^^

First, I set up a new virtual environment:

    sudo apt-get install python-virtualenv

    cd ~/Documents

    mkdir virtual_environments

    cd virtual_environments

    virtualenv --no-site-packages formhub

    source formhub/bin/activate

Second, I cloned the repo:

    cd ~/Documents

    git clone git@github.com:modilabs/formhub.git

Install the requirements:

    cd formhub

    pip install numpy --use-mirrors

    pip install -r requirements.pip

Install Mongodb:

    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10

    echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' >> /etc/apt/sources.list

    sudo apt-get update
    
    sudo apt-get install mongodb-10gen

If you don't already have a Java Runtime Environment installed this is
necessary for running ODK Validate. A *.jar file used to validate
XForms.

    sudo apt-get install default-jre

To create a database for your development server do the following:

    python manage.py syncdb

    python manage.py migrate

And now you should be ready to run the server:

    python manage.py runserver


Contributing
------------

If you would like to contribute code please read:

https://github.com/modilabs/formhub/wiki/Contributing-Code-to-Formhub


