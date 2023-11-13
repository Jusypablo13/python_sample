#!/bin/bash

echo Ingresa la ruta del directorio base:
read directorio_base

if [ ! -d "$directorio_base" ]; then
  echo "El directorio base no existe."
  exit 1
fi

directorios_encontrados=$(find "$directorio_base" -type d)
echo "Directorios encontrados debajo de $directorio_base:"
echo "$directorios_encontrados"

