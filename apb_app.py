import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image 

password= st.text_input('Airtel Payments Bank')
if password == "Airtel Payments Bank":
	image_url='posterityfinal.png'
	image= Image.open(image_url) 
	st.image(image,width=350)


	DATA_URL= 'file1.xlsx'

	#@st.cache(persist =True)
	def load_data():
		data = pd.read_excel(DATA_URL)
		return data


	data = load_data()

	clients= data['Client'].value_counts()
	#titles
	st.title('Client Report FY 2020-2021')
	st.sidebar.title('%s  '% (clients.index[0]))

	st.markdown('### By Posterity Better Solutions')
	st.sidebar.markdown('### A Review of the past year ')

	st.sidebar.markdown("### Number Of Positive Coneversions, Negative Conversions, and Pending Conversions")

	#newdataframe
	status_count= data['Status'].value_counts()
	status_count=pd.DataFrame({'Status':status_count.index, 'Count':status_count.values})


	st.markdown('### Number Of Positive Conversions, Negative Conversions And Pending Conversions')
	st.write('\n\n')
	st.write('\n\n As can be seen, out of **85** total selections:\n\n **24** Candidates were Positively Converted \n\n **45** Candidates were not Converted \n\n **3** Candidate Conversions are still Pending ')
	if st.sidebar.checkbox('Visual',True, key=4):
		fig1=px.pie(status_count, values='Count',names='Status')
		st.plotly_chart(fig1)



	st.sidebar.markdown("### Level Of roles Worked On")


	level_roles = data['Level'].value_counts()
	level_conversion=data.groupby('Level').count()
	level_conversion=level_conversion.loc[:,"Joining TAT"]
	level_roles = pd.DataFrame({'Level Of Roles':level_roles.index, 'Count Of Selections': level_roles.values, 'Count Of Joinings': level_conversion.values })
	st.markdown("### Level of Roles Worked On")
	st.write('Posterity worked on over **100** skills and roles for Airtel Payments Bank. \n\n Maximum hiring was done for the Backend Devloper Role and Java as the skill' )
	st.write('Hiring was done for three levels, **Junior Level** for Offered CTC < 15 LPA, **Middle Level** for offered CTC Between 15 LPA to 35 LPA, and **Senior Level** for Offered CTC > 35 LPA, Roles. \n\n **43** Selections were done for the Junior Level roles. \n\n **39** Selections were done for the Middle Level Roles. \n\n **3** Selections were done for Senior Level roles')
	st.write('Hover Over the Graph to Know the Number of Selections and Joinings for each Level.')
	if st.sidebar.checkbox('Visual',True,key=1):
		fig2=px.area(level_roles, x='Level Of Roles', y= 'Count Of Selections',hover_name='Level Of Roles',hover_data=['Count Of Selections','Count Of Joinings'])

		st.plotly_chart(fig2)


	#st.write(level_conversion)


	st.sidebar.markdown("### Selection TAT")


	selection_tat_count= data['Selection TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	selection_tat_count=pd.DataFrame({'Selection TAT':selection_tat_count.index,'Days':selection_tat_count.values})

	#st.write(selection_tat_count)
	st.markdown('### Selection TAT')
	st.write("Selection Turn Around Time (TAT) represents the Time in terms of **Days** taken by Airtel Payments Bank to select a submitted candidate")
	st.write("**26** Days were taken on an average for a selection. \n\n**225** days was the maximum number of days that was taken for a selection \n\n **0** days was the minimum number of days that was taken for a selection")
	if st.sidebar.checkbox('Visual',True,key=2):
		fig3=px.bar(selection_tat_count,x='Selection TAT',y='Days', color='Days', text='Days',title='Max, Average and Min TAT For Selection', hover_name='Selection TAT',hover_data=['Days'])
		fig3.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig3.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig3.update_layout(hovermode='x')


		st.plotly_chart(fig3)

	st.sidebar.markdown("### Offer TAT")
	#select= st.sidebar.selectbox('Visualization',['Bar Graph'], key=1)
	offer_tat_count= data['Offer TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	offer_tat_count=pd.DataFrame({'Offer TAT':offer_tat_count.index,'days':offer_tat_count.values})

	#st.write(offer_tat_count)
	st.markdown('### Offer TAT')
	st.write("Offer Turn Around Time (TAT) represents the time in terms of **Days** taken by Airtel Payments Bank to convert a selection to Offer")
	st.write("**9** Days were taken on an average to convert a selection to an offer. \n\n Maximum **61** Days were taken for the same. \n\n Minimum **0** Days were taken")

	if st.sidebar.checkbox('Visual',True,key=3):
		fig4=px.bar(offer_tat_count,x='Offer TAT',y='days', color='days',text='days',title='Max, Average and Min TAT For Offer Conversion',hover_name='Offer TAT',hover_data=['days'])
		fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside',width=0.4)
		fig4.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		fig4.update_layout(hovermode='x')
		st.plotly_chart(fig4)


	st.sidebar.markdown('### Joining TAT')

	joining_tat_count=data['Joining TAT'].describe().loc[['mean','min','max']].round(decimals=0)
	joining_tat_count=pd.DataFrame({'Joining TAT':joining_tat_count.index,'days':joining_tat_count.values})
	st.markdown('### Joining TAT')
	st.write("Joining Turn Around Time (TAT) represents the time in terms of **Days** taken by Airtel Payments Bank to convert the status of a candidate from Offer to Joining")
	st.write("**25** Positive Conversions took place,\n\n **51** Days on an average were taken for an Offer a Joining after offer confirmation \n\n**7** Days were the minimum number of days taken for the same \n\n **102** days were the maximum number of days taken for a joining.")
	if st.sidebar.checkbox('Visual',True,key=5):
		fig5=px.bar(joining_tat_count,x='Joining TAT',y='days', color='days',text='days',title='Max,Average and Min TAT for Joining', hover_name="Joining TAT",hover_data=['days'])
		fig5.update_traces(texttemplate='%{text: .2s}', textposition='outside',width=0.4)
		fig5.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
		st.plotly_chart(fig5)





	st.sidebar.header('Word Cloud')

	word_category= st.sidebar.radio('Display Word Cloud for Skill',('Skill','Role'))

	st.set_option('deprecation.showPyplotGlobalUse', False)
	if st.sidebar.checkbox('Word Cloud',True,key=5):
		st.header('Word Cloud for %s category' % (word_category))
		df1=data[data['Role']== word_category]
		df= data[data['Skill'] == word_category]
		words= (' '.join(data['Skill'])+' '.join(data['Role']))
		wordcloud=WordCloud(stopwords=STOPWORDS, background_color='white', height=200,width=500).generate(words)
		plt.imshow(wordcloud)
		plt.xticks([])
		plt.yticks([])
		st.pyplot()
	st.write('As can be seen, this is a WordCloud of all the skills and Roles for which Posterity worked on for Airtel Payments Bank')



	st.write("\n\n_____________________________________________________________________________________________________________________")
	st.subheader('With that We thank %s  '% (clients.index[0])) 
	st.write('for their association with Posterity Solutions for FY 2020-21. \n\n We hope the interactive dashboard could give you an insight on the Client Engagement, our values are founded on. \n\n We look forward to a long and mutually fruitful association with you. \n\n Regards Posterity ')
	st.image(image,width=150)
else:
	st.write('Wrong Password')


