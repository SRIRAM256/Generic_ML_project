from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e.'
def getReqirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',' ')  for req in requirements]

        requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
    name="ML_generic",
    version="0.0.1",
    author="sriram",
    packages=find_packages(),
    install_requires=getReqirements('requirements.txt')
)