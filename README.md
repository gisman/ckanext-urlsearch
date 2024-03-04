[![Tests](https://github.com/gisman/ckanext-urlsearch/workflows/Tests/badge.svg?branch=main)](https://github.com/gisman/ckanext-urlsearch/actions)

# ckanext-urlsearch

Search dataset URLs of all data portals in the gimi9 search box.


## Requirements

Python 3.8.10

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.6 and earlier | not tested    |
| 2.7             | not tested    |
| 2.8             | not tested    |
| 2.9             | yes           |
| 2.10            | yes           |


## Installation

To install ckanext-urlsearch:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com/gisman/ckanext-urlsearch.git
    cd ckanext-urlsearch
    pip install -e .
	pip install -r requirements.txt

3. Add `urlsearch` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload


## Config settings

None at present

## Developer installation

To install ckanext-urlsearch for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/gisman/ckanext-urlsearch.git
    cd ckanext-urlsearch
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests

None at present

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
