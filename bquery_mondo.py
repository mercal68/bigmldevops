import pandas as pd

from google.cloud import bigquery

def my_query(request):
    df_query = pd.read_gbq(request,project_id='mondo-tech-231015',dialect='standard')
    return df_query
  
  
  
if __name__ == "__main__":
    my_request = """ select * from compfood.pamtier limit 100 """
    print (len(my_query(my_request)))