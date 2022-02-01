PKG_NAME := qtbase
URL = https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtbase-everywhere-src-5.15.2.tar.xz
ARCHIVES = 

include ../common/Makefile.common

update:
	git -C ~/git/qtbase remote update -p
	git -C ~/git/qtbase diff origin/5.15.2..origin/kde/5.15 > new.patch~
	git -C ~/git/qtbase shortlog origin/5.15.2..origin/kde/5.15 > qtbase-stable-branch.patch~
	cat new.patch~ >> qtbase-stable-branch.patch~
	! diff qtbase-stable-branch.patch qtbase-stable-branch.patch~ > /dev/null
	mv qtbase-stable-branch.patch~ qtbase-stable-branch.patch
	rm -f *.patch~
	$(MAKE) bumpnogit
	git commit -m "stable update" -a
#	test -n "$(NO_KOJI)" || $(MAKE) koji-nowait
