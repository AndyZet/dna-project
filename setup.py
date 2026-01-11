from setuptools import setup, find_packages

setup(
    name="genealogy-dna-analysis",
    version="0.1.0",
    description="Genealogical DNA Analysis Workspace",
    author="Andrzej Radzimowski",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[
        "biopython>=1.81",
        "pysam>=0.21",
        "scikit-allel>=1.7",
        "pandas>=1.5",
        "numpy>=1.24",
        "scipy>=1.10",
        "scikit-learn>=1.2",
        "matplotlib>=3.7",
        "seaborn>=0.13",
        "plotly>=5.13",
        "geopandas>=0.12",
        "folium>=0.14",
        "sqlalchemy>=2.0",
        "psycopg2-binary>=2.9",
        "pymongo>=4.3",
    ],
)
