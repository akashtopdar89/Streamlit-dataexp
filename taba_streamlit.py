import streamlit as st
import pandas as pd
import numpy as np

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import nltk

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


import warnings
warnings.filterwarnings('ignore')
showWarningOnDirectExecution = 'false'




col2, col3 = st.columns([6,1])


with col2:
	st.header('TABA Streamlit Group Assignment')

	st.sidebar.title('Explore Dataset')

	

with col3:
	st.image('ISB_logo.png')

def explore(df):
	st.write('Scroll down to explore more about data')
	st.write('Data:')
	st.write(df)
	df_types = pd.DataFrame(df.dtypes, columns=['Data Type'])
	numerical_cols = df_types[~df_types['Data Type'].isin(['object', 'bool'])].index.values
	print(numerical_cols)
	df_types['Count'] = df.count()
	df_types['Unique Values'] = df.nunique()
	df_types['Min'] = df[numerical_cols].min()
	df_types['Max'] = df[numerical_cols].max()
	df_types['Average'] = df[numerical_cols].mean()
	df_types['Median'] = df[numerical_cols].median()
	df_types['St. Dev.'] = df[numerical_cols].std()
	st.write('Summary:')
	st.write(df_types.astype(str))

def transform(df):
	
	df_cat = df.select_dtypes(include='object')
	cols = st.multiselect('Columns', df_cat.columns.tolist(), df_cat.columns.tolist())
	df = df[cols]
	st.write('Select a column from Sidebar Dropdown to see wordcloud')
	stopwords = set(STOPWORDS)
	stopwords.update(['us', 'one', 'Uber', 'will', 'said', 'now', 'well', 'man', 'may', 'little', 'say', 'must', 'way', 'long', 'yet', 'mean','put', 'seem', 'asked', 'made', 'half', 'much', 'certainly', 'might', 'came'])
	llist = st.sidebar.selectbox("Select Column", cols)
	col_one_list = df[llist].tolist()
	str1 = ""
	# traverse in the string 
	for i in col_one_list:
		str1 += i

	wordcloud = WordCloud( background_color = 'white',max_words = 100, max_font_size = 256,).generate(str1)

	fig, ax = plt.subplots(figsize = (12, 8))
	ax.imshow(wordcloud)
	plt.axis("off")
	st.pyplot(fig)


def histogram_df(df):

	df_numerical = df.select_dtypes(include='int64')
	cols = st.multiselect('Columns', df_numerical.columns.tolist(), df_numerical.columns.tolist())
	df = df[cols]
	llist = st.sidebar.selectbox("Select Column", cols)
	print(llist,'here')
	col_one_list = df[llist].tolist()
	print(len(col_one_list))
	for i in col_one_list: #Since VARS is a list, it does one element at a time from the list
		# print(i)
		x_label = i
    #Labelling the X axis
		fig=px.histogram(df, x = i, labels = {'x' : x_label, 'y' : 'Count'})
		# Defining the plotly object of a histogram
		
		st.plotly_chart(fig)

def get_df(file):
	extension = file.name.split('.')[1]
	if extension.upper() == 'CSV':
		df = pd.read_csv(file, encoding='cp1252')
	elif extension.upper() == 'XLSX':
		df = pd.read_excel(file, engine='openpyxl')
	elif extension.upper() == 'PICKLE':
		df = pd.read_pickle(file)
	return df


def main():

	st.write('A general purpose data exploration app')
	file = st.sidebar.file_uploader("Upload file", type=['csv',	'xlsx', 'pickle'])
	if not file:
		st.write('Upload excel or csv file to explore')
		st.sidebar.write("Upload a .csv or .xlsx file to get started")
		st.sidebar.subheader('Group Members:')
		st.sidebar.write('Akash Topdar - ')
		st.sidebar.write('Lalith Sharma - ')
		st.sidebar.write('Prajukta Pradhan - ')
		st.sidebar.write('Pranjal Kumar Srivastava - ')
		st.sidebar.write('Sumith Tatipally - ')
		return
	df = get_df(file)
	task = st.sidebar.radio('Navigation', ['Explore', 'WordCloud'], 0)
	if task == 'Explore':
		explore(df)
	# elif task=='Histogram':
	# 	histogram_df(df)
	else:
		dd=transform(df)
		# st.write(dd)



# st.sidebar.image("ISB_logo.png", use_column_width=True)




main()

