import setuptools
import os
'''
with open("README.md", "r") as fh:
    long_description = fh.read()
'''
setuptools.setup(
    name="readable_password",
    version="1.1",
    author="Logamurugan Pilavadi",
    author_email= "splogamurugan@gmail.com",
    description = "a password generator that creates easy-to-remember / readable / pronounceable passwords",
    long_description= "a password generator that creates easy-to-remember / readable / pronounceable passwords",
    long_description_content_type="text/markdown",
    url="https://github.com/splogamurugan/readable_password",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
