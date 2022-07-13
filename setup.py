from setuptools import setup, find_packages

setup(
    name='MyInsuranceApp',
    version='0.3',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.md').read(),
    url='https://github.com/CT2-DEVOPS-Team2/myinsuranceapp',
    author='Ipanema',
    author_email='myemail@example.com'
)
