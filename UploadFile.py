import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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












    #
    # def CountPlot(self, column_target, hue=None):
    #     sns.set(style="darkgrid")
    #     return sns.countplot(x=column_target, data=self.df, hue=hue, palette='pastel')
    #
    # def HeatMapCorr(self):
    #     sns.set(style="darkgrid")
    #     sns.set(font_scale=0.6)
    #     corr = self.df.corr()
    #     return sns.heatmap(corr, annot=True, annot_kws={"size": 7}, linewidths=.5)
    #
    # def DistPlot(self, column_target):
    #     sns.set(style="darkgrid")
    #     return sns.distplot(self.df[column_target], color='c')
    #
    # def PairPlot(self, hue=None):
    #     sns.set(style="darkgrid")
    #     return sns.pairplot(self.df, hue=hue, palette="coolwarm")
    #
    # def BoxPlot(self, column_x=None, column_y=None, hue=None):
    #     sns.set(style="darkgrid")
    #     return sns.boxplot(x=column_x, y=column_y, hue=hue, data=self.df, palette="Set3")
    #

