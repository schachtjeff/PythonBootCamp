student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
#for (key, value) in student_dict.items():
#    print(f"{key}: {value}")

import pandas as pd
student_df = pd.DataFrame(student_dict)
print(student_df)

# Loop through a df, not great/useful
for (key, value) in student_df.items():
    print(key, value)

# Use a pandas iter of dataframe
for (index, row) in student_df.iterrows():
    #print(index, row)
    print(row.score)
    print(row.student)