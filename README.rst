This is very simple package template only
=========================================

First, in ``requirements.txt`` define requirements for your projects.

Second, fill properly ``setup.py`` file,

- ``name='''<package-name>'''``
- ``long_description='''<some-description>'''``
- ``version='''<version>'''``
- ``url='''<url-to-your-project'''``
- etc

Example console script:

.. code-block:: python

   entry_points={
     'console_scripts': [
       'my_python_script = my_package_name.submodule.main:main',
       'other_script = my_package_name.submodule.main:other'
     ]
   }
