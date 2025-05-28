.PHONY: all
all:
	lit multiple-of-7.py -Dcurrent_second=$(shell date +%s) -Dtest_retry_attempts=20 -vv --debug