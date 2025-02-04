# 4NL3 Project

Toxicity Classification NLP Project
Group 5 - Jackson Lippert - Emma Wigglesworth - Damien Cheung - Evan Placenis

## <span style="color:red">SENSITIVE CONTENT DISCLAIMER</span>

Our project contains sensitive contents including the following:

- Non Toxic
- Toxicity/Severe Toxicity
- Identity Attacks
- Sexual Harassment
- Insults
- Proafanity including racial slurs
- Threats to people's safety

If you are uncomfortable reading any of the above then contact the course instructor to possibly switch assignment.

## Annotation Guidelines / Data Structure

Each instance in our dataset corresponds to a tweet made on the X platform. The dataset is stored in the "dataset" folder, and each file corresponds to one subsection of the dataset to be annotated.

Each file contains \_\_\_\_ samples to be annotated.

Our data is in .csv format, which can be opened in Microsoft Excel (or whatever you want) for easy annotating. The first row displays the categories to which you will refer when going through the annotation instructions. The first column of each row refers to the Tweet that is in text format. The following 7 columns represent the seven classes that the annotation will fall under. The annotator is to provide one label per row, marked with a "1" and leave the rest of the columns blank.

## Data Source

All of the data was gathered from the free Kaggle Toxic Tweet Dataset (https://www.kaggle.com/datasets/ashwiniyer176/toxic-tweets-dataset).

## Data Processing Prodecure

The bulk of the preprocessing steps are seperated into two distict functions ("create_data_frame()" and "split_data_frame_into_files()") while the remaining two functions are used to display relevant information about the processed data.

The program begins by reading the Kaggle dataset and defining 3 final varaibles. These varaibles are used to dictate the number of files to be created, how many files contain duplicated data, and set the total size of the dataset (all files combined). The Toxic Tweet Kaggle datset is already split into binary classes (toxic vs non-toxic). Since our dataset consists of 7 classes (seen above) and majority of the classes consist of varying levels of toxic tweets, we must gather much more data from the toxic data compared to the non-toxic data. The variables mentioned above are used to deterimine the exact number of toxic and non-toxic tweets to be sampled from the existing kaggle dataset, along with how many duplicate samples will be created.

The "create_data_frame()" function is the first function that is called. It reads the kaggle df and samples the correct amount of data from both the toxic and non-toxic class. After this, it concatenates these two dataframes into a single "balanced" dataframe. The dataframe is then shuffled before being returned. After gathering the balanced dataframe, the dataframe is sliced into two parts. The first part represents the data that will be duplicated amoung all 7 files, while the remainder of the dataframe is split into 8 parts.

The last step of the program calls the "split_data_frame_into_files()" function with a custom header (which will be displayed on the first row of each csv file for the annotator). This function will loop 8 times and concatenate the duplicated rows to each data split (replacing the existing rows in its spot). On the 8th loop it does not concatenate the duplicated rows to the split. Each loop writes the dataframe to a .csv file and stores it in the dataset folder.
