#!/bin/sh
# Get name and version from Makefile
eval `sed -En '/^PKG_NAME\s*:?=\s*/s//PKG_NAME=/p
/URL\s*:?=\s*/{s///;s,.*-([0-9.]+)\.tar.xz,VERSION=\1,p;}' Makefile`

CHANGES_FILE=https://code.qt.io/cgit/qt/$PKG_NAME.git/plain/dist/changes-$VERSION?h=v$VERSION

rm -f NEWS ChangeLog
wget -O ChangeLog "$CHANGES_FILE" || \
    echo > ChangeLog "No changelog file found for $PKG_NAME $VERSION"
