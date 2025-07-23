## makefile automates the build and deployment for python projects


## Build sytem
#
PROJ_TYPE =		python
PROJ_MODULES =		python/doc python/package python/deploy
INFO_TARGETS +=		appinfo
CLEAN_ALL_DEPS +=	distclean


## Project
#
DIST_ENTRY =		./dist.py


## Includes
#
include ./zenbuild/main.mk


## Target
##
.PHONY:			appinfo
appinfo:
			@echo "app-resources-dir: $(RESOURCES_DIR)"

# create the distribution model and probank database
.PHONY:			dist
dist:
			$(DIST_ENTRY) clean
			$(DIST_ENTRY) package

# remove derived objects
.PHONY:			distclean
distclean:
			$(DIST_ENTRY) clean
