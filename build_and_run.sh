#!/bin/bash
set -e

sudo docker run --rm -it $(sudo docker build -q .) /bin/bash
