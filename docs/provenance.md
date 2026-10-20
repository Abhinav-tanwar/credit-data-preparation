# Source and changes

Credit Data Preparation was refactored from the author-supplied Python notebook into a reusable module, a clean demonstration notebook, and focused validation checks. Original files are preserved locally. Embedded notebook outputs were cleared rather than presented as newly reproduced results. Student identifiers, personal phone numbers, source-machine paths, and names from illustrative records are excluded.

New commits describe the actual work done now; original analysis dates are not fabricated.

## Corrections and interpretation

Fixes dataframe-wide fillna calls to column-specific preprocessing; fits imputers and encoders on training rows only; handles unseen categories and division by zero. Renames amount / percent_of_income to amount_per_income_percent because this denominator is not actual annual income. No predictive accuracy is claimed. Original dataset unavailable; synthetic records demonstrate the workflow.
