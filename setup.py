try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


install_requires = [
    "boto3 >= 1.0.1",
    "pyrax >= 1.9.2"
]

setup(name="object_storage",
      version="0.7.3",
      description="Python library for accessing files over various file transfer protocols.",
      url="https://github.com/ustudio/storage",
      packages=["storage"],
      install_requires=install_requires)
