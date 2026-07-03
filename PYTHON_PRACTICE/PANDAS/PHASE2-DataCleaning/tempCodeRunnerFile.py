def missing(self):
        print("\nTHE TOTAL NUMBER OF MISSING VALUES IN EACH COLUMN IS : \n", self.df.isnull().sum())
        print("\nTHE TOTAL NUMBER OF MISSING VALUES  IN THE WHOLE DATA FRAME IS :\n" , self.df.isnull().sum().sum())
        print("\nTHE ROWS HAVING ATLEAST ONE MISSING VALUES: \n" , self.df[self.df.isnull().any(axis=1)])
        self.df["salary"] = self.df["salary"].fillna(self.df["salary"].mean())
        self.df["experience"]=self.df["experience"].fillna(0)
        self.df["department"]=self.df["department"].fillna("Unknown")
        self.df["name"]=self.df["name"].fillna("Missing")
        return self.df

pp=Panda_practice(df)
print(pp.missing())