"""Credit preprocessing; no credit-approval model or lending decision logic."""
import argparse
from common import *
from sklearn.model_selection import train_test_split
NUMERIC=['months_loan_duration','age','amount','percent_of_income']
CATEGORICAL=['credit_history','checking_balance','employment_duration']

def clean_schema(data):
    d=data.copy();required=NUMERIC+CATEGORICAL+['default']
    if missing:=set(required)-set(d):raise ValueError(f'Missing columns: {sorted(missing)}')
    for c in NUMERIC:d[c]=pd.to_numeric(d[c],errors='coerce')
    d=d.dropna(subset=['default']).drop_duplicates()
    return d

def engineered_features(data):
    d=data.copy();d['amount_log']=np.log(d['amount'].where(d['amount']>0))
    # Source denominator is an installment/income percentage, not annual income.
    d['amount_per_income_percent']=d['amount'].div(d['percent_of_income'].where(d['percent_of_income']>0))
    d['age_band']=pd.cut(d.age,[0,30,50,np.inf],labels=['Young','Middle-Aged','Senior'],right=False).astype(object)
    return d

def run(input_path,output='outputs'):
    raw=pd.read_csv(input_path);d=clean_schema(raw);x=engineered_features(d.drop(columns='default'));y=d['default']
    train,test=train_test_split(d.index,test_size=.2,random_state=42,stratify=y)
    prep=preprocessor(NUMERIC+['amount_log','amount_per_income_percent'],CATEGORICAL+['age_band'])
    xt=prep.fit_transform(x.loc[train]);xv=prep.transform(x.loc[test])
    amount=d.loc[train,'amount'].dropna();q1,q3=amount.quantile([.25,.75]);iqr=q3-q1
    z=(amount-amount.mean())/amount.std(ddof=0)
    report={'data_kind':'synthetic demonstration' if Path(input_path).name.startswith('synthetic_') else 'user-supplied data','rows':len(d),'training_rows':len(train),'test_rows':len(test),'missing_before_imputation':d[NUMERIC+CATEGORICAL].isna().sum().to_dict(),'encoded_features':int(xt.shape[1]),'training_iqr_outliers':int(((amount<q1-1.5*iqr)|(amount>q3+1.5*iqr)).sum()),'training_zscore_outliers':int((z.abs()>3).sum()),'finite_transformed_values':bool(np.isfinite(xt).all() and np.isfinite(xv).all()),'target_distribution':{str(k):int(v) for k,v in y.value_counts().items()},'scope':'preprocessing only; no default prediction accuracy claimed'}
    assert set(train).isdisjoint(test) and report['finite_transformed_values']
    return save_report(output,report)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',default='data/synthetic_credit.csv');p.add_argument('--output',default='outputs');a=p.parse_args();print(json.dumps(run(a.input,a.output),indent=2))
