"""Setup for flashcards XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}

setup(
    name='flashcards-xblock',
    version='0.1',
    description="Flashcards XBlock allowes the editor to add a list of \
                quesitions and answers (separated by a comma) which are \
                then displayed as flashcards.",
    packages=[
        'flashcards',
    ],
    install_requires=[
        'XBlock',
        'Django',
    ],
    entry_points={
        'xblock.v1': [
            'flashcards = flashcards:FlashcardsXBlock',
        ]
    },
    package_data=package_data("flashcards", ["static", "public"]),
)
