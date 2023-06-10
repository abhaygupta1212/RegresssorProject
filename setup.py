from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_packages(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =  [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements

setup(  
    name = "RegressorProject",
    version = "0.0.1",
    author= "Abhay Gupta",
    author_email="abhaygupta.xyz@gmail.com",
    packages=find_packages(),
    install_requires = get_packages("requirements.txt")
)