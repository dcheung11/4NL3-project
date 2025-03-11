# Data

Our data is in .csv format. 

The first row displays the categories:
- Non Toxic
- Toxicity/Severe Toxicity
- Identity Attacks
- Sexual Harassment
- Insults
- Proafanity including racial slurs
- Threats to people's safety
- Sexually Explicit

The first column of each row refers to the Tweet that is in text format.

The following is a representation of the dataset

| Tweets To Be Annotated | Non_Toxic |Toxicity|Severe_Toxicity|Identity_Attack|Insult|Profanity|Threat|Sexually_Explicit|
|------------------------|-----------|---|---|---|---|---|---|---|
| Tweet                  | 0,1       | ...|
| Tweet               | ... |
| Tweet               | 
| Tweet               | 
| Tweet                  | 
| Tweet                  |
| Tweet                  | 
| Tweet                  | 

The dataset is sent to the candidate model as:
- `X`: a `np.ndarray` of shape `(num_samples, num_features)`,
- `y`: a `np.ndarray` of shape `(num_samples)`, representing the labels in dense format.
