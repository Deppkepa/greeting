from setuptools import setup, find_packages

setup(
   name='setup_test_hello',
   version='1.0',
   description='Тестовая функция привествия пользователя по имени для изучения setup.',
   license='CC0-1.0 license',
   author='Deppkepa',
   author_email='dasha.sisimirova@bk.ru',
   url='https://github.com/Deppkepa/greeting.git',
   packages=find_packages(),
   install_requires=['pytest','numpy'],
   extras_require={
        'test': [
            'pytest'
        ],
   },
   python_requires='>=0',
)
