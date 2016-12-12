"""The setup for my donation_manager."""

from setuptools import setup

setup(
    name="donation_manager",
    description="An implmentation of the donation manager.",
    version=0.1,
    author="Colin Lamont",
    author_email="colinlamont@gmail.com",
    license="MIT",
    py_modules=['donation_manager'],
    package_dir={'': 'src'},
    install_requires=['tox', 'tabulate'],
    extras_require={
        "test": ["pytest", "pytest-watch", "pytest-cov"]
    },
)
