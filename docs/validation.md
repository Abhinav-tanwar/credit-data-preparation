# Execution and validation

Executed with Python 3.12 using the versions pinned in requirements.txt. Program run completed successfully. Generated notebook cells passed Python syntax compilation; the notebook wrapper calls the same validated module. Full notebook execution in a separate Jupyter kernel was not performed.

```text
test_column_imputation_and_unseen_categories (test_analysis.CreditTest.test_column_imputation_and_unseen_categories) ... ok
test_zero_denominator_and_negative_amount (test_analysis.CreditTest.test_zero_denominator_and_negative_amount) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.010s

OK
```

Input/output data were checked for required fields, finite values, and appropriate synthetic-versus-supplied provenance. Output files contain aggregate metrics or non-personal examples; row-level clinical predictions are not published.
