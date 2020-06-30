import setuptools

setuptools.setup(
    name='commands-generator',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/commands-generator']
)
