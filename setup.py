import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='teslalavista',
    version='0.1',
    scripts=['teslalavista'],
    author="Shaun Gehring",
    author_email="shaungehring@me.com",
    description="A python client for the Tesla API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shaungehring/TeslaLaVista",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
     ],
 )
