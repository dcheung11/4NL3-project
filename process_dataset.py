import pandas as pd
import csv
import numpy as np
import os

# ----------------- helper functions --------------------------
def dislay_count(df):
    # Count occurrences of toxic (1) and non-toxic (0)
    toxicity_counts = df["Toxicity"].value_counts()

    # Display counts
    print("Toxic Tweets (1):", toxicity_counts.get(1, 0))
    print("Non-Toxic Tweets (0):", toxicity_counts.get(0, 0))

def test_file_size(n_duplicate, split_dfs):
    total_size = 0
    for i, split_df in enumerate(split_dfs):
        print(f"Split {i+1} Length: {len(split_df)}")
        total_size += len(split_df)
    print(f"Duplicate Length: {n_duplicate}")
    print(f"Total Length: {total_size}")
    #assert total_size == DATASET_SIZE

#---------------  Create data frame of tweets of proper size and toxic ratio  ----------------
def create_data_frame(df, num_toxic, num_non_toxic ):
    df["tweet"] = df["tweet"].str.replace("\n", "").str.strip()

    toxic_tweets = df[df["Toxicity"] == 1]["tweet"]
    non_toxic_tweets = df[df["Toxicity"] == 0]["tweet"]

    sampled_toxic = toxic_tweets.sample(n=num_toxic, random_state=42)
    sampled_non_toxic = non_toxic_tweets.sample(n=num_non_toxic, random_state=42)

    balanced_dataset = pd.concat([sampled_toxic, sampled_non_toxic])
    balanced_dataset = balanced_dataset.sample(frac=1, random_state=42).reset_index(drop=True)#shufle the dataset

    return balanced_dataset

#---------------  handle df splitting and handling of dulicate rows and put that data into csv files  ----------------
def split_data_frame_into_files(duplicated_rows, split_dfs, n_duplicate, custom_header):
    os.makedirs("dataset/", exist_ok=True) 
    for i in range(8):
        #replace the first n_duplicate rows with the saved duplicate rows for the first 7 splits
        if i < 7:
            split_dfs[i] = pd.concat([duplicated_rows, split_dfs[i].iloc[n_duplicate:]], ignore_index=True)

            split_dfs[i] = split_dfs[i].to_frame(name="tweet")
            final_split = pd.concat([custom_header, split_dfs[i]], ignore_index=True)
        final_split.to_csv(f"dataset/tweets_data_{i+1}.csv", index=False, header=False, encoding="utf-8", quoting=1)




                               ########       #######
 #---------------------------- ##       main       ##--------------------------------------------------
                               #######        #######
df = pd.read_csv('toxic-tweets-dataset/TweetDataset.csv')

TOTAL_SPLITS = 8
NUM_FILES_DUPLICATED = 7 #amount of files duplicate lines will appear in
DATASET_SIZE = 1920 #15 seconds per tweet = 4 tweets per minute = 240 per hour = 1920 tweets in total


#need to add n_duplicate back because the dataset is splitted 8 ways from after duplicated are extracted, they will then overwrite the fist lines
n_duplicate = round(DATASET_SIZE * 0.15 // NUM_FILES_DUPLICATED)
num_toxic = int((DATASET_SIZE + n_duplicate) * (6/7))
num_non_toxic = int((DATASET_SIZE + n_duplicate) * (1/7))

balanced_dataset = create_data_frame(df, num_toxic, num_non_toxic)
duplicated_rows = balanced_dataset.iloc[:n_duplicate]
remaining_dataset = balanced_dataset.iloc[n_duplicate:]

split_dfs = np.array_split(remaining_dataset, TOTAL_SPLITS)

custom_header = pd.DataFrame([[
    "Tweets To Be Annotated",  # Tweet column (adjust if needed)
    "Non_Toxic", "Toxicity", "Severe_Toxicity", "Identity_Attack", "Insult", "Profanity", "Threat" , "Sexually_Explicit" # Separate columns
  ]])

# (adjust if needed)
custom_header.columns = ["tweet", "Non-Toxic", "Toxicity", "Severe Toxicity", "Identity Attack", "Insult", "Profanity", "Threat", "Sexually Explicit"]

split_data_frame_into_files(duplicated_rows=duplicated_rows,
                            split_dfs= split_dfs,
                            n_duplicate= n_duplicate,
                            custom_header= custom_header)


# dislay_count(df)
# test_file_size(n_duplicate, split_dfs)