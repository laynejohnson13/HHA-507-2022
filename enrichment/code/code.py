import pandas as pd 

########################
### load in the data 
########################
patients = pd.read_csv('enrichment/example_data/patients.csv')
patients

medications = pd.read_csv('enrichment/example_data/medications.csv')

patients.columns
medications.columns

patients['Id']
medications['PATIENT']

#### we are going to take medications table and 
#enrich it with some patient information from out patient table

df_patients_small = patients[['Id', 'CITY', 'STATE', 'COUNTY', 'ZIP']]
print(df_patients_small.sample(10).to_markdown())

df_medications_small = medications [['PATIENT', 'CODE', 'DESCRIPTION', 'BASE_COST', 'PAYER']]
print(df_medications_small.sample(10).to_markdown())


combined_df = df_medications_small.merge(df_patients_small, how= 'left', left_on='PATIENT', right_on='Id')

combined_df = pd.merge(df_medications_small, df_patients_small, how ='left', left_on= 'PATIENT', right_on = 'Id')

combined_df.columns


###save new combined df 
combined_df.to_csv ('enrichment/example_data/combined_df.csv')

###
med_df = medications [['PATIENT', 'PAYER']]
pay_df = payers_df[['Id', 'CITY']]
pat_df = patients[[['Id', 'CITY', 'STATE', 'COUNTY', 'ZIP']]]

##### ANOTHER combined df but merging the other way

combined_df = df_patients_small.merge(df_medications_small, how= 'left', left_on='Id', right_on='PATIENT')


###load in payers

payers_df = pd.read_csv('enrichment/example_data/payers.csv')
payers_df

payers_df.shape
payers_df.head(5)

### creating another new df 

payers_df = payers_df[['NAME', 'Id', 'AMOUNT_COVERED']]

payers_df.shape

patients_payers = df_patients_small.merge(payers_df_small, how = 'left', left_on = 'Id', right_on = 'Id')

patients_payers.to_csv ('enrichment/example_data/patients_payers.csv')



########################
### merge examples 
# add medications to patients
########################
patients_simple = patients[['Id', 'SSN']]
medications_simple = medications[['PATIENT', 'DESCRIPTION']]

patients_medications = patients_simple.merge(medications_simple, 
            how='left', 
            left_on='Id', right_on='PATIENT')

print(patients_medications.head(5).to_markdown())

patients_medications = patients_medications.drop(columns=['PATIENT'])

########################
### concat examples 
########################

patient_sample_1 = patients.sample(n=10)
patient_sample_2 = patients.sample(n=10)

patients_s1_s2_concat = pd.concat([patient_sample_1, patient_sample_2])