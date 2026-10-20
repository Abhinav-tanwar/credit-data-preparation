import sys,unittest
from pathlib import Path
import pandas as pd,numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from analysis import clean_schema,engineered_features
from common import preprocessor
class CreditTest(unittest.TestCase):
 def test_column_imputation_and_unseen_categories(self):
  train=pd.DataFrame({'age':[20.,30.,np.nan],'credit_history':['good',np.nan,'poor']})
  prep=preprocessor(['age'],['credit_history'],scale=False);prep.fit(train)
  test=pd.DataFrame({'age':[9999.,np.nan],'credit_history':['new','good']})
  actual=prep.transform(test)
  self.assertEqual(actual[1,0],25);self.assertEqual(prep.named_transformers_['numeric'].named_steps['impute'].statistics_[0],25)
 def test_zero_denominator_and_negative_amount(self):
  d=pd.DataFrame({'age':[30.],'amount':[-1.],'percent_of_income':[0.]});r=engineered_features(d)
  self.assertTrue(pd.isna(r.amount_log.iloc[0]));self.assertTrue(pd.isna(r.amount_per_income_percent.iloc[0]));self.assertEqual(d.amount.iloc[0],-1)
if __name__=='__main__':unittest.main()
