#!/bin/bash
# Genera el .rpm dentro de un contenedor Fedora (no requiere rpmbuild en el host).
set -e
cd "$(dirname "$0")"
mkdir -p dist-rpm
podman run --rm -v "$PWD":/src:Z fedora:latest bash -c 'mkdir -p /work && cd /work
  set -e
  dnf install -y -q rpm-build python3-pip binutils mesa-libGL libxkbcommon-x11 xcb-util-cursor >/dev/null
  cp -r /src/app.py /src/logica.py /src/styles.qss /src/fuentes /src/requirements.txt /work/
  pip install -q -r requirements.txt
  pyinstaller --noconfirm --clean --windowed --name Calculadora7 \
    --add-data "styles.qss:." --add-data "fuentes:fuentes" app.py >/dev/null
  mkdir -p ~/rpmbuild/SOURCES
  cp -r dist/Calculadora7 ~/rpmbuild/SOURCES/
  rpmbuild -bb /src/packaging/calculadora7.spec
  cp ~/rpmbuild/RPMS/x86_64/*.rpm /src/dist-rpm/
'
ls -l dist-rpm
