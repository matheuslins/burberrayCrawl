from setuptools import setup, find_packages

setup(
    name='burberryCrawl',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = burberryCrawl.settings']},
)
