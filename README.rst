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

..note::

    If you are using a remote server, or need to access it via an intranet, do::

        sudo python manage.py runserver 0.0.0.0:80

    and navigate to: http://yourownaddress.com/


Contributing
------------

If you would like to contribute code please read:

https://github.com/modilabs/formhub/wiki/Contributing-Code-to-Formhub


