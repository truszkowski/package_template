#!/bin/bash

if [ $# -ne 1 ]
then
	echo "usage: $0 <pypi-server>"
	exit 1
fi

python setup.py sdist upload -r $1
