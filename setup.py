from setuptools import setup,find_packages
from typing import List
''' 
Essesntial for the setup of the project, this file is used to install the dependencies and the package itself.
and metadata and dependecies and more
'''
requirements:List[str]=[]
def get_requirements()->List[str]:
    try:
        with open ('requirements.txt','r') as f:
            lines=f.readlines()
            for line in lines:
                if line.strip() and not line.startswith('-e'):
                    requirements.append(line.strip())
    except FileNotFoundError:
        print(f"Error reading requirements.txt: File not found.")
    return requirements

setup(
    name='NetworkSecurity',
    version='0.0.1',
    description='A package for network security analysis and machine learning.',
    author='Uday Kiran',
    author_email='peddiudaykiran61@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)

