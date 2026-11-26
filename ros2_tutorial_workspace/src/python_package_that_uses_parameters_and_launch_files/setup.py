from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'python_package_that_uses_parameters_and_launch_files'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # This is specific to the launch file
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ryan',
    maintainer_email='meretciel.fr@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'amazing_quote_configurable_publisher_node = python_package_that_uses_parameters_and_launch_files.amazing_quote_configurable_publisher_node:main'
        ],
    },
)
