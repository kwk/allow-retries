.PHONY: all
all:
	LIT_OPTS="-Dmaximum_retries_per_test=4000" lit multiple-of-7.py -vv --debug
