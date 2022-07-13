
from setuptools import setup, find_packages

setup(
    name='myinsuranceapp',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/CT2-DEVOPS-Team2/myinsuranceapp.git',
    author='IpanemaGroup',
    author_email='myemail@example.com'
)
