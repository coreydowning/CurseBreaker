import setuptools

setuptools.setup(
    name="CurseBreaker",
    version="3.10.2",
    author="AcidWeb",
    author_email="pawelj@iosphe.re",
    url="https://github.com/AcidWeb/CurseBreaker",
    packages=[
        'prompt_toolkit',
        'cloudscraper',
        'checksumdir',
        'pyperclip',
        'requests',
        'markdown',
        'bbcode',
        'rich',
        'lupa'
    ],
    python_requires='~=3.8',
)
