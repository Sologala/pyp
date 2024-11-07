from setuptools import setup, find_packages

setup(
    name='pyp',
    version='0.0.1',
    install_requires=[
        'numpy',
        'ffmpeg-python',
        'importlib-metadata; python_version<"3.10"',
    ],
    packages=find_packages(
    ),
    entry_points={
        'console_scripts': [
            'pyp = pyp.entry:main_entry',
        ]
    }
)
