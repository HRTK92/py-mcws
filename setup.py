from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='py-mcws',
    version="1.0.2",
    description="Minecraft Bedrock WebSocket",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='HRTK92',
    url="https://github.com/HRTK92/py-mcws",
    license='MIT',
    install_requires=_requires_from_file('requirements.txt'),
    packages=['py_mcws']
)
