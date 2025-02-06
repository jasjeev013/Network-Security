from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt') as f:
            lines = f.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
                    
    except FileNotFoundError:
        print("Requirements file not found")
        
    return requirement_lst


setup(
    name='Network Security',
    version='0.0.1',
    author='Jasjeev',
    author_email='jasjeev1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)