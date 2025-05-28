.PHONY: all
all:
	lit multiple-of-7.py -vv --debug -Dmaximum_retries_per_test=4000
