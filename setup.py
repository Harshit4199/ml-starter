from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."
def get_requirements(file_name):
    """
    paramenters: requirement.txt path
    return: list of requirement packages
    """
    with open(file_name) as file_obj:
        requirements = file_obj.readlines()
        requirements = [line.replace('\n', '') for line in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='ml-starter',
    version="0.1",
    author="Harshit",
    author_email="hp.harshit4199@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)