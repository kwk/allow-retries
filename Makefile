.PHONY: all
all:
	lit allow-retries.py -Dcurrent_second=$(shell date +%s) -Dtest_retry_attempts=20 -vv --debug