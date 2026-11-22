from setuptools import find_packages, setup

package_name = 'python_package_that_uses_the_services'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'what_is_the_point_server_node=python_package_that_uses_the_services.what_is_the_point_server_node:main',
            'what_is_the_point_client_node=python_package_that_uses_the_services.what_is_the_point_client_node:main'
        ],
    },
)
