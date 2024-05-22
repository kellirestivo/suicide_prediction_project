import pandas as pd
##Read CSV into pandas as a data frame to be more easily manipulated
##MORTALITY DATASET represents US suicides between the years 2005-2015
#new_names = ["education", "month_of_death", "sex", "exact_age", "age_group1", "age_group2", "place_of_death_and_decedents_status", "marital_status", "day_of_week_of_death", "injury_at_work", "place_of_injury", "358_cause_recode", "race1", "race_recode_3", "race_recode_5", "hispanic_originrace", "record_condition_1_desc", "record_condition_2_desc", "record_condition_3_desc", "entity_condition_1_desc", "entity_condition_2_desc", "entity_condition_3_desc" "method", "race_new"]
def clean_up_data(filename, extension):
    data = pd.read_csv("~/Desktop/mortality_data.csv")
    data.head()

#Drop all columns in which 1% or more of the rows contain the value NaN
#(The dataset has >420,000 entries, so 1% is a substantial number of rows)
    new_data = data.dropna(thresh = len(data) - (len(data) * 0.01), axis = 1)

#Drop all columns in which all rows contain the same value (these columns are uninformative)
    cols = list(new_data)
    nunique = new_data.apply(pd.Series.nunique)
    cols_to_drop = nunique[nunique == 1].index

    new_data = new_data.drop(cols_to_drop, axis = 1)

#Remove unecessary columns
    new_data = new_data.drop(["resident_status", "education_reporting_flag", "age_recode_12",
                           "age_recode_27", "manner_of_death", "method_of_disposition", "autopsy",
                            "activity_code", "icd_code_10th_revision", "113_cause_recode",
                           "number_of_entity_axis_conditions", "entity_condition_1",
                           "entity_condition_2", "number_of_record_axis_conditions",
                           "record_condition_1", "record_condition_2", "race", "race_recode_3",
                           "hispanic_origin", "record_condition_2_desc", "entity_condition_1_desc",
                           "race_recode_5", "hispanic_originrace_recode",
                           "place_of_death_and_decedents_status", "358_cause_recode",
                           "entity_condition_2_desc", "record_condition_1_desc",
                           "day_of_week_of_death", "month_of_death"], axis = 1)
#list(new_data3.columns.values)
    new_data = new_data.dropna()
#Rename column headers to more simple identifiers
    new_data.columns = ["education", "sex", "age", "age_group", "marital_status", "year",
                     "injury_at_work", "place", "icd_code", "method", "race"]
#Rearrange columns to place demographic/social criteria first, followed by suicide details
    new_data = new_data[["education", "sex", "age", "age_group", "marital_status", "race",
                       "year","injury_at_work","place", "icd_code", "method"]]
    new_data

    ##Drop output features
input_feature_df = new_data.drop(["age","year", "injury_at_work", "place", "icd_code",
                                  "method"], axis = 1)
#input_feature_df = input_feature_df[~input_feature_df."education".str.contains("")]


#Drop all rows that contain the value "unknown"
input_feature_df = input_feature_df[(input_feature_df[["education", "sex", "age_group",
                                                      "marital_status", "race"
                                                      ]] != "Unknown").all(axis = 1)]
#Drop all rows that lack information on any other feature
input_feature_df = input_feature_df[input_feature_df.age_group != "Age not stated"]
input_feature_df = input_feature_df[input_feature_df.marital_status != "Marital Status unknown"]
for col in input_feature_df:
    print(input_feature_df[col].unique())
#input_features = list(input_feature_df.columns)

#feature_dictionary = {}

input_feature_dictionary = {}
input_features = list(input_feature_df.columns)
input_feature_options = input_feature_df[col].unique()


for i in input_features:
    input_feature_dictionary[i] = input_feature_options[i]
