from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    """Read requirements.txt and return a list of packages."""
    
    with open(file_path) as f:
        requirements = [line.strip() for line in f.readlines()]
    # remove blank lines and the '-e .' entry
    return [r for r in requirements if r and r != HYPHEN_E_DOT]

setup(
    name='mlproject',
    version='0.0.1',
    author='Sayan',
    author_email='sayan@example.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)