from setuptools import setup, find_namespace_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='markipy',
    author='Marco T.',
    url='https://github.com/MarkNo1/MarkPy',
    version='0.0.3',
    license=license,
    description='MrkPy LIB',
    long_description=readme,
    packages=find_namespace_packages(include=['markipy', 'markipy.*']),
    entry_points={'console_scripts': ['markipy = markipy.script:Main']},
    install_requires=requirements,
    include_package_data=True,
    python_requires='>=3.7'
)
