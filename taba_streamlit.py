import streamlit as st
import pandas as pd
import numpy as np

from wordcloud import WordCloud
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

st.title('LAPPS Streamlit')

def explore(df):
	# DATA
	st.write('Data:')
	st.write(df)
	# SUMMARY
	df_types = pd.DataFrame(df.dtypes, columns=['Data Type'])
	numerical_cols = df_types[~df_types['Data Type'].isin(['object',
	           'bool'])].index.values
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
	# Select sample size
	# frac = st.slider('Random sample (%)', 1, 100, 100)
	# if frac < 100:
	# 	df = df.sample(frac=frac/100)
	# Select columns
	cols = st.multiselect('Columns', 
	                    df.columns.tolist(),
	                    df.columns.tolist())
	# print(cols)
	df = df[cols]
	# print(df[1])
	# df1 = df[cols].values()
	# option = st.selectbox(“Select option”, CHOICES.keys(), format_func=lambda x:CHOICES[ x ])
	# topic = st.selectbox('select topic',['topic1','topic2','topic3'])
	# Create some sample text
	# text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

	# Create and generate a word cloud image:
	# option = st.selectbox(cols) #option is stored in this variable
	llist = st.sidebar.selectbox("Select Column", cols)
	# years = df["year"].loc[df["make"] == llist]
	print(llist)
	col_one_list = df['Review'].tolist()
	str1 = ""
	# traverse in the string 
	for i in col_one_list:
	    str1 += i



	wordcloud = WordCloud().generate(str1)

	# # Display the generated image:
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")
	plt.show()
	st.pyplot()
	# st.set_option('deprecation.showPyplotGlobalUse', False)

	# return df


def get_df(file):
	# get extension and read file
	extension = file.name.split('.')[1]
	if extension.upper() == 'CSV':
		# df = pd.read_csv(file)
		df = pd.read_csv(file, encoding='cp1252')
	elif extension.upper() == 'XLSX':
		df = pd.read_excel(file, engine='openpyxl')
	elif extension.upper() == 'PICKLE':
		df = pd.read_pickle(file)
	return df

def main():
  # st.title('Explore a dataset')
  st.write('A general purpose data exploration app')
  file = st.sidebar.file_uploader("Upload file", type=['csv', 
                                               'xlsx', 
                                               'pickle'])
  if not file:
    st.sidebar.write("Upload a .csv or .xlsx file to get started")
    return
  df = get_df(file)
  task = st.sidebar.radio('Task', ['Explore', 'Transform'], 0)
  if task == 'Explore':
    explore(df)
  else:
    dd=transform(df)
    # st.write(dd)



# FILE_ADDRESS = st.sidebar.file_uploader('Upload file')
# This variable takes the filepath after a GUI window allows you to select files from a file explorer.

st.sidebar.image("ISB_logo.png", use_column_width=True)

st.sidebar.title('Explore Dataset')
# This is the title for the sidebar of the webpage, and stays static, based on current settings. 
# The column functionality which has been commented out further on allows the title of the main page to be dynamic.

main()
