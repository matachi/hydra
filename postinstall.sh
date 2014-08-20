#!/usr/bin/env bash

cd node_modules/bootstrap && npm install && cd -
virtualenv env
./env/bin/pip install Pygments
