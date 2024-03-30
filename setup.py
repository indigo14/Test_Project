# The setup script is the centre of all activity in building, distributing,
# and installing modules using the Distutils. The main purpose of the setup 
# script is to describe your module distribution to the Distutils, so that the
# various commands that operate on your modules do the right thing. As we saw 
# in section A Simple Example above, the setup script consists mainly of a call
# to setup(), and most information supplied to the Distutils by the module 
# developer is supplied as keyword arguments to setup().
# https://docs.python.org/3.11/distutils/setupscript.html
from setuptools import find_packages,setup #Find all the packages that are available in the project
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='Test_Project', #Name of the project
    version='0.0.1', #Version of the project
    author='Mike', #Author of the project
    author_email='michaelyardley7@gmail.com', #Author email
    packages=find_packages(), #Looks for __init__.py files in the directories and creates a package
    install_requires=get_requirements('requirements.txt') #List of all the dependencies that are required for the project
)      