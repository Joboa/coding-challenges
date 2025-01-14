from setuptools import setup, find_packages

setup(
    name='ccbf',
    version='0.1.0',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'psutil',
    ],
    entry_points={
        'console_scripts': [
            'ccbf=ccbf.main:main',
        ],
    },
    python_requires=">=3.7",
    description="Custom Command BrainF Interpreter",
    author="John Boamah",
    author_email="joboa2015@gmail.com",
)