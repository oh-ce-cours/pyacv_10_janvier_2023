from setuptools import setup

setup(
    name="funniest",
    version="0.2",
    description="Super blague",
    url="http://example.com/ahahah/",
    author="Matthieu Falce",
    author_email="clown@example.com",
    license="MIT",
    packages=["funniest"],
    zip_safe=False,
    entry_point={  # commandes qui seront installées
        "console_scripts": ["funniest-joke=funniest.command_line:main"],
    },
)
