from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(filename)->List[str]:
    """
    This function will return the list of requirements
    """
    req_list : List[str] = []
    try:
        with open(filename,'r') as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()
                ## ignore epty lines and -e .
                if requirement and requirement != HYPEN_E_DOT :
                    req_list.append(requirement) 
    except FileNotFoundError:
        print('requirements.txt is not found')

    return req_list

## print(get_requirements('requirements.txt'))

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author='Soumalla Tarafder',
    email = 'soumallatarafder@gmail.com',
    packages=find_packages(),
    install_requiers=get_requirements('requirements.txt')
)
