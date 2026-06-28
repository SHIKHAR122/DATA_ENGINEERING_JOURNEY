df=pd.DataFrame(admissions)
# class AdmissionCleaner:
#     def __init__(self,df):
#         self.df=df
#         self.duplicated_rows=0
#     def cleaner(self):
#         self.duplicated_rows=self.df.duplicated(subset="applicant_id").sum()
#         self.df = self.df.sort_values(by="score",na_position="last")
#         self.df=self.df.drop_duplicates(subset="applicant_id",keep="first")
#         overall_avg = self.df["score"].mean()
#         self.df["score"] = self.df["score"].fillna(overall_avg)
#         return self.df
    

#     def summary_data(self):
#         return self.duplicated_rows

# ac=AdmissionCleaner(df)
# print(ac.cleaner())
# print("THE TOTAL NUMBER OF ROWS REMOVED ARE :", ac.summary_data())