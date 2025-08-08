from skbuild import setup  # This line replaces 'from setuptools import setup'

setup(
    name="pyp",
    version="1.2.3",
    description="a minimal example package (cpp version)",
    author="The scikit-build team",
    license="MIT",
    packages=["hello"],
    python_requires=">=3.9",
)

# setup(
#     name='pyp',
#     version='0.0.1',
#     install_requires=[
#         'numpy',
#         'fire',
#         "imageio",
#         "pillow",
#         'importlib-metadata; python_version<"3.10"',
#     ],
#     packages=find_packages(
#     ),
#     entry_points={
#         'console_scripts': [
#             'pyp = pyp.entry:main_entry',
#         ]
#     }
# )
