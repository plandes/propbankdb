## makefile automates the build and deployment for python projects


## Build sytem
#
PROJ_TYPE =		python
PROJ_MODULES =		python/doc python/package python/deploy
CLEAN_ALL_DEPS +=	distclean


## Project
#
DIST_BIN ?=		./dist.py


## Includes
#
include ./zenbuild/main.mk


## Target
#
# create the distribution model and probank database
.PHONY:			dist
dist:
			@$(MAKE) $(PY_MAKE_ARGS) distclean
			@$(MAKE) $(PY_MAKE_ARGS) pyharn \
				PY_HARNESS_BIN=$(DIST_BIN) ARG=package

# remove derived objects
.PHONY:			distclean
distclean:
			@$(MAKE) $(PY_MAKE_ARGS) pyharn \
				PY_HARNESS_BIN=$(DIST_BIN) ARG=clean
