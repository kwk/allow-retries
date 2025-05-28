.PHONY: all
all:
	lit --debug -Dtest_retry_attempts=20 -vv allow-retries.py