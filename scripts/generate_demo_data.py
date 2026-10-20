"""Generate synthetic demo inputs. These are not recovered original records."""
from pathlib import Path
import numpy as np,pandas as pd
rng=np.random.default_rng(42);root=Path(__file__).resolve().parents[1];n=1200
duration=rng.integers(6,61,n).astype(float);age=rng.integers(18,76,n).astype(float);amount=np.round(rng.lognormal(7.8,.65,n),2)
default=rng.binomial(1,1/(1+np.exp(-(-2.5+.02*duration+.00006*amount))))
d=pd.DataFrame({'months_loan_duration':duration,'credit_history':rng.choice(['good','poor','limited'],n),'age':age.astype(object),'amount':amount,'checking_balance':rng.choice(['0 DM','1 - 200 DM','> 200 DM','unknown'],n),'percent_of_income':rng.integers(1,5,n),'employment_duration':rng.choice(['unemployed','< 1 year','1 - 4 years','4 - 7 years','> 7 years'],n),'default':default})
for c in ['months_loan_duration','credit_history','age']:d.loc[rng.choice(n,35,replace=False),c]=np.nan
d.loc[0,'age']='\\';d.to_csv(root/'data/synthetic_credit.csv',index=False)
print('Created 1200 synthetic credit demonstration records (seed=42).')
