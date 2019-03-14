import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mutationplanner',
    version='0.1',
    description='The funniest joke in the world',
    long_description=long_description,
    url='https://github.com/cssd2019/mutationplanner',
    license='MIT',
    packages=setuptools.find_packages(),
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
       'biopython',
       'numpy',
       'scipy',
       'matplotlib'
    ]
)
