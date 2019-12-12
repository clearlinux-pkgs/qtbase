#!/bin/sh
# Get name and version from Makefile
eval `sed -En '/^PKG_NAME\s*:?=\s*/s//PKG_NAME=/p
/URL\s*:?=\s*/{s///;s,.*-([0-9.]+)\.tar.xz,VERSION=\1,p;}' Makefile`

CHANGES_FILE=https://code.qt.io/cgit/qt/$PKG_NAME.git/plain/dist/changes-$VERSION?h=v$VERSION

git rm -f NEWS ChangeLog
if wget -O ChangeLog "$CHANGES_FILE"; then
    git add ChangeLog
fi
exit 0
