from setuptools import setup

setup(
  name='NFL_Draftkings',
  packages=['NFL_Draftkings'],
  version='3',
  description='Python wrapper around NFL api that calculates Draftkings scores for players',
  author='Tom Dodson',
  author_email='tcdodson@gmail.com',
  url='https://github.com/sharkiteuthis/NFL_Draftkings',
  download_url='https://github.com/sharkiteuthis/NFL_Draftkings/tarball/2',
  keywords=['nfl', 'draftkings', 'python', 'api', 'wrapper', 'player', 'scores', 'points'],
  classifiers=[],
  install_requires=['requests-cache'],
)
