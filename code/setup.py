from setuptools import setup


setup(name='thinkstats2',
      version='1.0',
      description="Library code for Think Stats, 2nd Edition packaged",
      author='Allen Downey',
      license="GPLv3",
      py_modules=['thinkstats2', 'thinkplot'],
      url='https://github.com/AllenDowney/ThinkStats2',
      install_requires=[
          'matplotlib',
          'numpy',
          'pandas',
          'scipy',
          ],
      )
