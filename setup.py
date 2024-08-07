import os
from setuptools import setup , find_packages

def read(*paths):
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()
    

def read_requeriments(path):
    return[
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#","gir+",'"','-'))
    ]


setup(
    name="dundie",
    version="0.1.0",
    description="Reward point System for dundle Mifflin",
    author="Moisés Filipe",
    packages=find_packages(),
    entry_points= {
        "console_scripts": [
            "dundie = dundie.__main__:main"
        ]
    },
    install_requires=read_requeriments("requirements.txt"),
    extras_require={
        "test": read_requeriments("requirements.test.txt"),
        "dev": read_requeriments("requirements.dev.txt"),
    }
)