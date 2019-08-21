import pandas as pd

from google.cloud import bigquery

def my_query(request):
    df_query = pd.read_gbq(request,project_id='wipro-idp-env',dialect='standard')
    return df_query
  
  
  
if __name__ == "__main__":
    my_request = """ select * from aramark_poc.PAM_with_tier_price limit 100 """
    print len(my_query(my_request))