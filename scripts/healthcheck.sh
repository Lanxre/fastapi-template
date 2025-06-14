#!/bin/sh
set -e

curl --fail --silent --show-error --connect-timeout 1 --max-time 2 http://localhost:3000/v1/health