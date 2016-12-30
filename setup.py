import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['-v']
        self.test_suite = True

    def run_tests(self):
        import pytest
        err_code = pytest.main(self.test_args)
        sys.exit(err_code)


setup(
    name='Flask-QRcode',
    version='0.9.0',
    license='MIT',
    description='A simple flask extension to render QR codes on template',
    long_description=open('README.md').read(),
    author='Marco Agner',
    author_email='marco@agner.io',
    url='https://github.com/marcoagner/Flask-QRcode',
    platforms='any',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Flask',
        'qrcode',
        'pillow'
    ],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=find_packages()
)
