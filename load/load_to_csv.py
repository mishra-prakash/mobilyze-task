import pandas
# import sys
# sys.path.append("")
class Load():
    def __init__(self):
        pass
    
    @staticmethod
    def to_csv(df,name=None):
        try:
            df = df.to_csv(f"./output/{name}.csv", index=False)
            print(f"{name}.csv created successfully!")
        except Exception as e:
            print(f"Got an error: {e}")