import setuptools

__version__ = "0.0.1"
    
setuptools.setup(
    name="chemicalParsers",
    version=__version__,
    author="S.Sosnin",
    author_email="sergey.sosnin@skoltech.ru",
    description="Chemical parsers",
    url="http://github.com/sergsb/chemicalParsers",
    packages=setuptools.find_packages(),
    package_data={'chemicalParsers': ['chemicalParsers/jserver/*']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'py4j',
    ],
    python_requires='>=3.6',
)
