from setuptools import setup

setup(
   name='SoftwareEngineering',
   version='1.0',
   description='HW 1',
   author=['Akshat Savla', 'Tilak Satra', 'Mohit Soni', 'Madiha Mansoo', 'Anagha Patil'],
   author_email=['asavla@ncsu.edu', 'tsatra@ncsu.edu', 'msoni@ncsu.edu', 'mmansoo@ncsu.edu', 'apatil28@ncsu.edu'],
   packages=['code', 'tests'],  #same as name
   long_description="""\
               Creating github repository files.
               .gitignore
               CODE-OF-CONDUCT.md
               CONTRIBUTING.md
               LICENSE.md
               README.md
               setup.py
               src/
                 __init__.py
           """,
   classifiers=[
      "License :: MIT License",
      "Programming Language :: Python",
      "Development Status :: Running",
      "Intended Audience :: Everyone",
      "Topic :: Software Engineering",
   ],
   keywords='requirements license python gitignore',
   license='MIT',
   install_requires=[
      'pytest',
   ],)