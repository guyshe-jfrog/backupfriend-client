import setuptools
import sys
from src.backupfriend.__init__ import __version__ as version
TOKEN="ghp_8Y67X222Q222zaE2EVf225VfKdCLpd181knb"

with open("README.rst", "r") as fh:
    long_description = fh.read()

P2APP_OPTIONS = {
    'argv_emulation': False,
    'site_packages': True,
    #'iconfile': 'appicon.icns',
    'packages': ["schedule", "encodings", "requests", "packaging",
                 "appdirs", "cryptography", "rdiff_backup"],
    'plist': {
        'CFBundleName': 'BackupFriend',
        'CFBundleDisplayName': 'BackupFriend',
        'LSUIElement': False,
    },
    'iconfile': 'src/backupfriend/images/icon.icns',
    'extra_scripts': ["/usr/local/bin/rdiff-backup"]
}
install_requires=[
         "PyYAML==5.2", "schedule", 'dataclasses;python_version<"3.7"', "appdirs", "cryptography", "pypubsub", "requests", "packaging"]

if sys.platform == "darwin":
    install_requires = ["wxPython", "schedule", "appdirs", "cryptography", "pypubsub", "pyyaml==5.2", "requests", "packaging"]


setuptools.setup(
    name="backupfriend",
    version=version,
    description="Read the latest Real Python tutorials",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/guysoft/BackupFriend",
    author="Guy Sheffer",
    author_email="gusyoft@gmail.com",
    license="GPLv3",
    py_modules=["backupfriendclient"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=setuptools.find_packages(where="src"),
    package_dir={
        "": "src",
    },
    data_files=[('images', ['src/backupfriend/images/icon.png']),
                ('config', ['src/backupfriend/config/config.yml', 'src/backupfriend/config/config-osx.yml', 'src/backupfriend/config/config-windows.yml']),
                ('res', ['src/backupfriend/res/main.xrc'])],
    include_package_data=True,
    install_requires=install_requires,
    entry_points={"console_scripts": ["backupfriend=backupfriendclient:run"]},
    app=['src/backupfriend-client.py'],
    options={'py2app': P2APP_OPTIONS},
    setup_requires=['py2app'],
)
