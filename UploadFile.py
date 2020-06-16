import streamlit as st
import io


class FileInfo:

    def __init__(self, dataframe):
        self.df = dataframe
        self.columns = dataframe.columns
        self.numerical_columns = [name for name in self.columns if
                                  (self.df[name].dtype == 'int64') | (self.df[name].dtype == 'float64')]

    def info(self):
        buffer = io.StringIO()
        self.df.info(buf=buffer)
        return buffer.getvalue()

    def info2(self, column_target):
        df = self.df[column_target].value_counts().to_frame().reset_index()
        df.sort_values(by='index', inplace=True, ignore_index=True)
        df.rename(columns={'index': column_target, '{}'.format(column_target): "Iterated"}, inplace=True)
        return df
