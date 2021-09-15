from setuptools import setup, find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='py-mcws',    #パッケージ名
    version="0.0.1",
    description="Minecraft Bedrock WebSocket",
    long_description="",
    author='HRTK92',
    url="https://github.com/HRTK92/py-mcws",
    license='MIT',
    classifiers=[
        "Development Status :: 1 - Planning"
    ],
    install_requires=_requires_from_file('requirements.txt'),
    packages=['py_mcws']   #パッケージのサブフォルダー
)