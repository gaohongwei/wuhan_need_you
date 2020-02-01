#!/bin/bash

# Test the uwsgi http protocol

uwsgi --socket 0.0.0.0:5000 --protocol=http -w deploy.wsgi:app

