# README

I try to find out how we can run LLVM `lit` tests and configure them to rerun
flaky tests.

## Artificial flakiness

When building LLVM and running its test we sometime experience flaky tests the
work the second time you run them.

To reproduce this flakyness I've created a test called `multiple-of-7.py`.

The `multiple-of-7.py` test file will only succeed (exit with `0`)
when the current second is a multiple of `7`.

When it succeeds it prints: `Current second IS a multiple of 7`.
When it fails it prints: `Current second is NOT a multiple of 7`

## Usage

Just run `make` to see how lit is called and `LIT_OPTS` is being used to specify
a newly introduced `maximum_retries_per_test` setting. This setting, if given is
then assigned to LIT's `test_retry_attempts` config variable, which internally
is read to fill a tests `allowed_retries` variable which controls for how often
a test execution can be repeated.

See [this upstream PR](https://github.com/llvm/llvm-project/pull/141851) to
introduce the `maximum_retries_per_test` setting to the `openmp` test directory.

### Example run

```
$ make
LIT_OPTS="-Dmaximum_retries_per_test=4000" lit multiple-of-7.py -vv --debug
lit: /usr/lib/python3.13/site-packages/lit/discovery.py:66: note: loading suite config '/home/fedora/src/allow-retries/lit.cfg.py'
lit: /usr/lib/python3.13/site-packages/lit/TestingConfig.py:142: note: ... loaded config '/home/fedora/src/allow-retries/lit.cfg.py'
lit: /usr/lib/python3.13/site-packages/lit/discovery.py:141: note: resolved input 'multiple-of-7.py' to 'allow-retries'::('multiple-of-7.py',)
-- Testing: 1 tests, 1 workers --
FLAKYPASS: allow-retries :: multiple-of-7.py (1 of 1)

Testing Time: 4.68s

Total Discovered Tests: 1
  Passed With Retry: 1 (100.00%)
```

Notice the `FLAYKYPASS:`.


