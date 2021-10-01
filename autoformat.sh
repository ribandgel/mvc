#! /bin/sh

autoflake --remove-all-unused-imports --remove-unused-variables --remove-duplicate-keys \
  --recursive --in-place players

isort players

flake8  players
 
black --line-length=119 players
