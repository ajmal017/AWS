import pandas as pd

def Renko(df):
    print(df.head(1).close[0])
    print(df.at[0,'close'])


def main():
    df = pd.read_pickle("one-month-1Min-SBI-21-June.pkl")
    Renko(df)


if __name__ == '__main__':
    main()

