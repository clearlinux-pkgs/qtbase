#!/bin/bash
set -e -o pipefail

PKG_NAME=qtbase
VERSION_START=5.15.2
STABLE_TAG=5.15

mkdir -p ~/git/qtstable
pushd ~/git/qtstable ; [ -d "$PKG_NAME" ] || git clone https://invent.kde.org/qt/qt/"${PKG_NAME}".git ; popd
git -C ~/git/qtstable/"${PKG_NAME}" remote update -p
git -C ~/git/qtstable/"${PKG_NAME}" diff origin/"${VERSION_START}"..origin/kde/"${STABLE_TAG}"  -- ':!.qmake.conf'  > new.patch~
[ -z "$(cat new.patch~)" ] && rm new.patch~ && exit
git -C ~/git/qtstable/"${PKG_NAME}" shortlog origin/"${VERSION_START}"..origin/kde/"${STABLE_TAG}" > "${PKG_NAME}"-stable-branch.patch~
cat new.patch~ >> "${PKG_NAME}"-stable-branch.patch~
diff "${PKG_NAME}"-stable-branch.patch "${PKG_NAME}"-stable-branch.patch~ > /dev/null && rm "${PKG_NAME}"-stable-branch.patch~ new.patch~ && exit
mv "${PKG_NAME}"-stable-branch.patch~ "${PKG_NAME}"-stable-branch.patch
rm -f *.patch~
make autospec
make koji-nowait
