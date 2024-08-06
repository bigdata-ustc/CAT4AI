from setuptools import setup, find_packages

setup(
    name='CAT',
    version='0.0.1',
    author='xxx',
    author_email='xxx@xxx.com',
    packages=find_packages(),
    url='xxx',
    install_requires=[
        'torch',
        'vegas',
        'numpy',
        'scikit-learn',
        'scipy',
    ],  # And any other dependencies foo needs
    entry_points={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)