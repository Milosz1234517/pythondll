from setuptools import setup, Distribution
 
 
class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True


setup(
    name='Interpolation',
    version='1.0',
    description='Interpolation',
    packages=['interpolation'],
    package_data={
        'interpolation': ['native.dll'],
    },
    distclass=BinaryDistribution
)