try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Perceptron Learning Helper',
    'author': 'Dhaby Xiloj',
    'url': 'github/dhabyx/learningPerceptron',
    'download_url': 'github',
    'author_email': 'dhabyx@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['perceptron'],
    'scripts': [],
    'name': 'learnPerceptron'
}

setup(**config)
