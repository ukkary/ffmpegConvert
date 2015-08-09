#!/bin/bash

if [[ ! -d $2 ]]; then
  mkdir -p output/$2
fi

ffmpeg -i input/$1 output/$1