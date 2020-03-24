### Thanks for Your Help!

Contributing is so kind of you. In ThinkStats2, all contributions, bug reports, bug
fixes, documentation improvements, enhancements and ideas are welcome.

The [GitHub "issues" tab](https://github.com/AllenDowney/ThinkStats2/issues)
contains some issues labeled "first PR". Those are open issues that would be a
good quick way to get started. Browse them to see if you want to get started on
one.

#### Bug Reports

  - Please include a short but detailed, self-contained Python snippet or
    explanation for reproducing the problem.

  - Explain what the expected behavior was, and what you saw instead.

##### Instructions for setting up a development environment

The ThinkStats2 project aims to to be compatible between Python 2.7 and 3.x,
so it is important to test in both platforms before submitting a pull request.
Anaconda is the recommended distribution to use to work on ThinkStats2; we will
assume that if you want to use another distribution or your own set up,
you can translate the instructions.

You can download Anaconda at https://www.continuum.io/Downloads for the full
install. You can also download a mini Anaconda install for a bare-bones
install -- this is good for a build server or if you don't have much space.
The mini Anaconda installs are available at https://conda.io/miniconda.html.

Once your Anaconda package is installed and available, create a Python 2.7
and 3.6 environment in Anaconda --

 - conda create -q -n thinkstats2-py27 python=2.7 scipy numpy matplotlib statsmodels patsy future jupyter seaborn
 - conda create -q -n thinkstats2-py36 python=3.6 scipy numpy matplotlib statsmodels patsy future jupyter seaborn

Each of these commands will take a bit of time -- give it a few minutes
to download and install the packages and their dependences. Once complete,
switch to each and install additional packages needed to run and test.

Activate the 2.7 environment and install nose and lifelines

 - source activate thinkstats2-py27
 - pip install nose lifelines

Activate the 3.6 environment and install nose and lifelines

 - source activate thinkstats2-py36
 - pip install nose lifelines

*For conda versions after 4.4 use `conda activate` instead of `source activate`*


Extras that are helpful --

 - runipy allows you to run IPython Notebooks on the command line which
   can help validating the code there without having to click through
   a browser session
 - flake8 for styles checks. PEP8 styles are not strictly enforced,
   but flake8 can call point out style and formatting fixes that can
   enhance readability
   
##### Run the tests

Tests are automatically detected and run with nose. To run them, use
the nosetests script that was made available when nose was installed
and run nosetests in the code directory so that the tests can find
the implementation code.

Note that one of the tests will generate a matplotlib image in a
new window and the window will need to be closed for the tests to
continue.

Start in the root directory where you have cloned the ThinkStats2 repository
and run for Python 2.7 --

 - conda activate thinkstats2-py27
 - cd code
 - nosetests

And then for Python 3.6 --

 - conda activate thinkstats2-py36
 - cd code
 - nosetests

##### Pull Requests

  - **Make sure the test suite passes** on your computer. To do so, run `nosetests` in the code directory.
  - Please reference relevant Github issues in your commit message using `GH1234`
    or `#1234`.
  - Keep style fixes to a separate commit to make your PR more readable.
  - Docstrings ideally follow the [sphinx autodoc](https://pythonhosted.org/an_example_pypi_project/sphinx.html#function-definitions)
  - Write tests.
  - When you start working on a PR, start by creating a new branch pointing at the latest
    commit on github master.
  - The ThinkStats2 copyright policy is detailed in the ThinkStats2 [LICENSE](https://github.com/AllenDowney/ThinkStats2/blob/master/LICENSE).

#### More developer docs

* We are working on it.

#### Meta
Note, this contributing file was adapted from the one at the
[pyrk](https://github.com/pyrk/pyrk) repo which was adapted from
the one at the [pandas](https://github.com/pydata/pandas) repo.
Thanks pyrk and pandas!
