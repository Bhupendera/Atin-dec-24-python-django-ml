from setuptools import setup, find_packages

setup(
    name="pytoolkit",
    version="1.0.0",
    description="A utility package for demonstration purposes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/pytoolkit",
    packages=find_packages(),
    install_requires=[
        "SQLAlchemy>=2.0.0",
        "pandas>=1.4.0",
    ],
    package_data={
        '': ['__pycache__/*.pyc'],  # Include only compiled files
    },
    exclude_package_data={
        '': ['*.py'],  # Exclude source .py files
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
