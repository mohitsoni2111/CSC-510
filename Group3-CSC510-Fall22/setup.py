from setuptools import setup

setup(
    name='Homework1-Group-3',
    version='0.1',
    description='Homework-Github repository',
    author='Nandini Mundra',
    author_email='nmundra@ncsu.edu',
    packages=['src', 'tests'],
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
            "Development Status :: Planning",
            "Intended Audience :: Developers",
            "Topic :: Software Engineering (CSC510)",
        ],
        keywords='requirements license python gitignore',
        license='MIT',
        install_requires=[
            'pytest',
        ],
        )

