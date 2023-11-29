# setup.py
from setuptools import setup, find_packages

setup(
    name='OTU_predictor',
    version='0.1',
    packages=find_packages(),
    package_data={'OTU_predictor': ['model/*.joblib']},
    install_requires=[
        'pandas',
        'scikit-learn',
        'joblib',
        'os',
    ],
)
