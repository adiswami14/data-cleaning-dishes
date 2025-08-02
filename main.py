import pandas as pd


def add_difference_column(df):
    df['staying_power'] = df['last_appeared'] - df['first_appeared']