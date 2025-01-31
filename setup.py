from setuptools import setup, find_packages

# Основні дані про пакет
NAME = "text_analyzer"
VERSION = "0.1.0"
DESCRIPTION = "A text analysis tool written in Python."
AUTHOR = "Your Name"
AUTHOR_EMAIL = "your.email@example.com"
URL = "https://github.com/yourusername/text-analyzer"

# Зависимости, які потрібно встановити
REQUIRES = [
    "matplotlib==3.4.3",
]

# Вказуємо шляхи до всіх необхідних файлів та директорій
PACKAGE_DATA = {
    '': ['*.txt', '*.rst'],
}

# Додаткові метадані
CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

# Інформація про пакет
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(where="src"),  # Знаходить всі пакети у директорії src
    package_dir={"": "src"},  # Повертаємося на рівень вище до директорії src
    install_requires=REQUIRES,
    package_data=PACKAGE_DATA,
    classifiers=CLASSIFIERS,
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'text_analyzer=src.main:main',  # Команда для запуску головного скрипту
        ],
    },
)