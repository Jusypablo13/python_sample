#!/bin/bash

cont=1
form=""

for arg in "$@"; do
  form+="$cont: $arg"
  if [ $cont -ne $# ]; then
    form+=", "
  fi
  cont=$((cont + 1))
done

echo $form
