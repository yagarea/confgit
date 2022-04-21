Introduction
=======


.. image:: https://readthedocs.org/projects/confgit/badge/?version=latest
   :target: https://confgit.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


.. image:: https://www.codefactor.io/repository/github/yagarea/confgit/badge/master
   :target: https://www.codefactor.io/repository/github/yagarea/confgit/overview/master
   :alt: CodeFactor


.. image:: https://img.shields.io/badge/python-3.x-green.svg
   :target: https://www.python.org/
   :alt: Python 3.x

.. image:: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat
   :target: http://makeapullrequest.com
   :alt: PRs Welcome


.. image:: https://img.shields.io/github/issues-pr/yagarea/confgit
   :target: https://github.com/yagarea/confgit/pulls
   :alt: PR info


.. image:: https://img.shields.io/github/issues/yagarea/confgit
   :target: https://github.com/yagarea/confgit/issues
   :alt: Open issues


.. image:: https://img.shields.io/github/stars/yagarea/confgit?style=social
   :target: https://github.com/yagarea/confgit/stargazers
   :alt: Repo stars


Confgit is a Git overhead for version control of your config files. The main difference between confgit and any other config file version system is its simplicity. It makes version control and migration of config files safe and easy.

How does it work?
-----------------

With confgit, you do not have to learn anything new, you only need to set up a directory where confgit will copy all files you register. After setup, you will have all your config files centralized in one directory where you can edit and maintain your config files with Git.

Features
--------

* **Centralization:** Manage files across multiple directories in one directory
* **Version control:** Track config files with Git without turning your entire filesystem into a Git repository
* **Import/Export:** Git allows you to easily push or clone your config files to and from a remote server to archive and share
  

Usage
-----

``init``
^^^^^^^^^^^^

Initialize a git repository for your config files in current directory and generates config file in ``~/.config/confgit.yml`` if you do not specify other location using ``--config`` argument.

.. code-block:: txt

   confgit init

.. code-block:: txt

   confgit init --config /alternative/location/of/config/file/confgit.yml

``sync``
^^^^^^^^^^^^

Writes content of complementary files of registered files to their origins.

.. code-block:: txt

   confgit sync

``update``
^^^^^^^^^^^^^^

Writes content of origins of registered files to their's complementary files.

.. code-block:: txt

   confgit update

``backup``
^^^^^^^^^^^^^^

Creates a zip file with backup of all files in confgit repository.

.. code-block:: txt

   confgit backup

You can specify the name of the backup file.

.. code-block:: txt

   confgit backup my_backup_monday.zip

If the name of the backup does not end with ``.zip`` it will be automatically added.

``include``
^^^^^^^^^^^^^^^

Registers a file or a directory into a confgit watch list.

.. code-block:: txt

   confgit include nvim.init

Including directories will register all its files recursively.

.. code-block:: txt

   confgit include ~/.config/

``exclude``
^^^^^^^^^^^^^^^

Excludes a file or directory from the registered files.

.. code-block:: txt

   confgit exclude zoom.conf

Excluding directories will exclude all its files recursively.

.. code-block:: txt

   confgit exclude .config/rofi/

*other*
^^^^^^^^^^^

Every other command will be called as git argument in directory with registered files.

``confgit pull`` -> ``git pull``

Optional Arguments
^^^^^^^^^^^^^^^^^^


* ``-h``\ , ``--help``                              - show this help message and exit
* ``-c $config_path``\ , ``--config $config_path``  - load alternative config
* ``--debug``                                   - show additional information for debugging
