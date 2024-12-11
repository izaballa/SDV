from setuptools import setup

package_name = 'vesc'

setup(
    name=package_name,
    version='1.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'pyserial', 'pyvesc'],  # Añadir aquí pyserial y pyvesc
    zip_safe=True,
    maintainer='natxozm13',
    maintainer_email='izaballa@ikerlan.es',
    description='A ROS2 node for VESC',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vesc_node = vesc.vesc_node:main',
        ],
    },
)
