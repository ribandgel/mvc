#! /bin/sh

autoflake --remove-all-unused-imports --remove-unused-variables --remove-duplicate-keys \
  --recursive --in-place players

isort players

flake8 --ignore E203,E501,W503 players
 
black --line-length=100 players
