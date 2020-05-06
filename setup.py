from setuptools import setup, find_packages

requires = [
    'Flask',
    'requests'
]

setup(
    name='cors anywhere',
    version='1.0',
    description='cors anywhere',
    author='Avinash Bhosale',
    author_email='abhosale@ambrosialinfo.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
)
