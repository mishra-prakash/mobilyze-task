import pandas

class Load():
    def __init__(self):
        pass

    def to_csv(self,name, df):
        try:
            df = df.to_csv(f"{name}.csv", index=False)
            print(f"{name}.csv created successfully!")
        except Exception as e:
            print(f"Got an error: {e.message}")