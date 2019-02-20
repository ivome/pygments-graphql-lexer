from setuptools import setup, find_packages

setup(
    name='graphqllexer',
    packages=find_packages(),
    entry_points=
    """
    [pygments.lexers]
    graphqllexer = graphqllexer.lexer:GraphqlLexer
    """,
)
