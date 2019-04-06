#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Dependencies
import requests
from requests import Session
import csv
import copy
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine


# In[10]:


# Construct url strings
immu_url = "https://data.wa.gov/api/views/kck7-yb2v/rows.csv?accessType=DOWNLOAD"
wa_county_url = "https://data.wa.gov/api/views/tecv-qzfm/rows.csv?accessType=DOWNLOAD"


# In[11]:


# Extract immunization data
immunization_df = pd.read_csv(immu_url, parse_dates=True)
immunization_df.head()


# In[12]:


# Extract Washington county data
wa_county_df = pd.read_csv(wa_county_url, parse_dates=True)
wa_county_df.head()


# In[13]:


immunization_df.columns


# In[14]:


immunization_df = immunization_df[['County', 'School_Year', 'Reported_enrollment', 'Number_complete_for_all_immunizations']].copy()

# Rename the columns
immunization_df = immunization_df.rename(columns = {'County':'county', 
                                                    'School_Year':'school_year', 
                                                    'Reported_enrollment':'number_reported',
                                                    'Number_complete_for_all_immunizations':'number_completed'})

# Take a peak
immunization_df.head()


# In[15]:


wa_county_df.columns


# In[16]:


wa_county_df = wa_county_df[['COUNTY', 'POP_2016']].copy()

# Rename the columns
wa_county_df = wa_county_df.rename(columns = {'COUNTY':'county', 'POP_2016':'pop_2016'})

wa_county_df.head()

