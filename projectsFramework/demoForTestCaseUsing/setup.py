try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'My project',
    'author':'shawn.li',
    'url':'toBeFilled',
    'dowload_url':'toBeFilled',
    'author_email':'shawn.yim@foxmail.com',
    'version':'0.01',
    'install_requires':['nose'],
    'packages':['computer'],
    'scripts',[],
    'name':'skeleton'
}

setup(**config)