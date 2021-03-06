from setuptools import find_packages, setup
setup(
    name="opti_lib",
    packages=find_packages(),
    maintainer_email="rohitrajak1907@gmail.com",
    version="1.0.0",
    description="Python library to Optimize the cost of Transportation in U/G mines",
    author="Rohit Rajak",
    install_requires=["cffi","numpy"],
    author_email="rohitrajak1907@gmail.com",
    license="MIT",
    python_requires='>=3.8'
)