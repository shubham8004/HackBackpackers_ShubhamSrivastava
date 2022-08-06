#!/usr/bin/env python
# coding: utf-8

# In[50]:


get_ipython().system('pip install sql-metadata-lineage')


# In[51]:


import sql_metadata_lineage


# In[52]:


def get_originating_tables(sql_script):
    try:
        table_map, column_map = sql_metadata_lineage.get_metadata(sql_script)
    except Exception as ex:
        raise ex
    return table_map, column_map


# In[41]:


# Example Test
table_map, column_map = get_originating_tables('''SELECT investments.month_nm AS month_nm,
           acquisitions.companies_acquired,
           investments.companies_rec_investment
      FROM (
            SELECT acq.acquired_month_nm AS month_nm,
                   COUNT(DISTINCT acq.company_permalink) AS companies_acquired
              FROM tutorial.crunchbase_acquisitions acq
             GROUP BY 1
           ) acquisitions

      FULL JOIN (
            SELECT invst.funded_month_nm AS month_nm,
                   COUNT(DISTINCT invst.company_permalink) AS companies_rec_investment
              FROM tutorial.crunchbase_investments invst
             GROUP BY 1
           ) investments

        ON acquisitions.month_nm = investments.month_nm''')


# In[43]:


print(table_map)


# In[44]:


print(column_map)

