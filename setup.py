from setuptools import setup, find_packages

import roboticslogger

setup(
    name=roboticslogger.__appname__,
    version=roboticslogger.__version__,

    description='Async Logging System for Space Concordia Robotics Division',
    long_description=open('README.rst').read(),
    url='http://www.github.com/space-concordia-robotics/robotics-logger',
    license='MIT',

    author='Simon Symeonidis',
    author_email='lethaljellybean@gmail.com',

    install_requires=["colorama>=0.3.3"],

    packages=['roboticslogger'],

    scripts=['roboticslogger/bin/roboticslogger-test'],

    test_suite="test"
)
