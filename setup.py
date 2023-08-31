from setuptools import setup, find_packages

# Reading long description from README.md file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="UniswapGraphQLClient",
    version="1.0.0",
    author="Florian Letellier",
    author_email="flo.letellier@proton.me",
    description="A Python client for Uniswap using GraphQL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BlockchainProphet/UniswapGraphQLClient",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    test_suite="tests",
)
