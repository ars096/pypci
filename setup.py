
import setuptools

setuptools.setup(
    name = 'pypci',
    version = __import__('pypci').__version__,
    description = 'PCI driver for python',
    url = 'https://github.com/ars096/pypci',
    author = 'Atsushi Nishimura',
    author_email = 'ars096@gmail.com',
    license = 'MIT',
    keywords = '',
    packages = [
        'pypci',
    ],
    install_requires = ['portio'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
