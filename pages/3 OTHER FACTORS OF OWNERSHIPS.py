import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import time
df = pd.read_csv('D:\MISY\Homework\Assignment\\Cleaned_DS_Jobs.csv')
# Add up all required skills
df["add_skills"] = df['python'] + df['excel'] + df['hadoop'] + df['spark'] + df['aws'] + df['tableau'] + df['big_data']

# 设置网页标题
st.title('Analysis and Display of Data Science Job Information Based on Streamlit')

# 展示一级标题
st.header('3. Analysis of Factors Related to Ownership and Other Variables in Data Science ')

def get_sizenum(x: str):
    num = x.split(" ")
    if len(num) == 4:
        if "+" in num[0]:
            num[0] = num[0].replace("+", "")
        if "+" in num[2]:
            num[2] = num[2].replace("+", "")
        fir = float(num[0])
        end = float(num[2])
        return (fir + end)
    else:
        return None


dfa = df
dfa['Size_num'] = dfa['Size'].apply(get_sizenum)
dfa['if_seniority'] = dfa['seniority'].apply(lambda x: 1 if x == 'senior' else 0)
#Variables required for the first graph
df_hot = dfa[['Rating', 'same_state', 'company_age', 'Size_num', 'add_skills', 'if_seniority', 'avg_salary']]
# Data cleaning
df_hot1 = df_hot[df_hot['company_age'] != -1]
# used in the second picture
df_hot2 = df_hot1[['Rating', 'company_age', 'Size_num']]
df_hot21 = df_hot2[df_hot2['company_age']<=50]
df_hot21 = df_hot2[df_hot2['Rating']>=3]
# Used in the third picture
df_hot22 = df_hot2[df_hot2['company_age']<=50]
df_hot22 = df_hot2[df_hot2['Rating']<3]
# four
df_hot23 = df_hot2[df_hot2['company_age']>50]
df_hot23 = df_hot2[df_hot2['Rating']>=3]
# five
df_hot24 = df_hot2[df_hot2['company_age']>50]
df_hot24 = df_hot2[df_hot2['Rating']<3]

# Remove some irrelevant data
df_re1 = df_hot[['company_age','Size_num']]
df_re1 = df_re1[df_re1['company_age']!= -1]
df_re1.dropna(subset=['Size_num'], inplace=True)
# distinct num and size

df_skill = df[['job_simp','Type of ownership','python','excel','hadoop','spark','aws','tableau','big_data','add_skills']]
df_skill1 = df_skill[['python','excel','hadoop','spark','aws','tableau','big_data']]

df_skill2 = df_skill[['job_simp', 'Type of ownership', 'add_skills']]
df_skill2 = df_skill2[df_skill2['job_simp']!='director']
df_skill2 = df_skill2[df_skill2['Type of ownership'].isin(['Company - Public', 'Company - Private'])]

df_skill3 = df[['job_simp','python']]

def draw_hot_ratingall():
    k = 6
    cols = df_hot1.corr().abs().nlargest(k + 1, 'Rating')['Rating'].index
    cm = df_hot1[cols].corr()
    plt.figure(figsize=(8, 5))
    plt.title('Rating_relative')
    sns.heatmap(cm, annot=True, cmap='Blues')
    st.pyplot(plt)

def draw_hot_age_size1():
    # Set style
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 8))
    # Draw a scatter plot
    plot = sns.scatterplot(data=df_hot21, x="company_age", y="Size_num", hue="Rating", palette="coolwarm", s=100,
                           marker='o')
    # Add titles and tags
    plot.set_title('Rating vs. company_age and Size_num', fontsize=16)
    plot.set_xlabel('Company Age', fontsize=12)
    plot.set_ylabel('Size Number', fontsize=12)
    # Adjust background and grid
    plot.set_facecolor('lightgray')
    plot.grid(True, linestyle='--', color='white')
    # Adjust legend
    plot.legend(title="Rating", loc="upper right", fontsize=10)
    # Hide borders
    sns.despine()
    st.pyplot(plt)

def draw_hot_age_size2():
    # Set style
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 8))
    # Draw a scatter plot
    plot = sns.scatterplot(data=df_hot22, x="company_age", y="Size_num", hue="Rating", palette="coolwarm", s=100,
                           marker='o')
    # Add titles and tags
    plot.set_title('Rating vs. company_age and Size_num', fontsize=16)
    plot.set_xlabel('Company Age', fontsize=12)
    plot.set_ylabel('Size Number', fontsize=12)
    # Adjust background and grid
    plot.set_facecolor('lightgray')
    plot.grid(True, linestyle='--', color='white')
    # Adjust legend
    plot.legend(title="Rating", loc="upper right", fontsize=10)
    # Hide borders
    sns.despine()
    st.pyplot(plt)
def draw_hot_age_size3():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 8))
    
    plot = sns.scatterplot(data=df_hot23, x="company_age", y="Size_num", hue="Rating", palette="coolwarm", s=100,
                           marker='o')
    
    plot.set_title('Rating vs. company_age and Size_num', fontsize=16)
    plot.set_xlabel('Company Age', fontsize=12)
    plot.set_ylabel('Size Number', fontsize=12)
   
    plot.set_facecolor('lightgray')
    plot.grid(True, linestyle='--', color='white')
    
    plot.legend(title="Rating", loc="upper right", fontsize=10)
    
    sns.despine()
    st.pyplot(plt)
def draw_hot_age_size4():
    
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 8))
    
    plot = sns.scatterplot(data=df_hot24, x="company_age", y="Size_num", hue="Rating", palette="coolwarm", s=100,
                           marker='o')
    
    plot.set_title('Rating vs. company_age and Size_num', fontsize=16)
    plot.set_xlabel('Company Age', fontsize=12)
    plot.set_ylabel('Size Number', fontsize=12)
    
    plot.set_facecolor('lightgray')
    plot.grid(True, linestyle='--', color='white')
    
    plot.legend(title="Rating", loc="upper right", fontsize=10)
    
    sns.despine()
    st.pyplot(plt)

def draw_size_age():
    plt.figure(figsize=(8, 6))
    sns.regplot(data=df_re1[(df_re1['company_age'] <= 50) & (df_re1['Size_num'] <= 2000)], x='company_age',
                y='Size_num', color='green')
    plt.xlim((0, 50))
    plt.ylim((0, 1750))
    plt.xlabel('Company Age')
    plt.ylabel('Size Number')
    plt.title('Relationship between Company Age(less than 50) and Size Number(less than 2000)')
    st.pyplot(plt)

def draw_size_age2():
    plt.figure(figsize=(8, 6))
    sns.regplot(data=df_re1[(df_re1['Size_num'] > 2000)], x='company_age', y='Size_num', color='green')
    # plt.xlim((0,50))
    # plt.ylim((0,1750))
    plt.xlabel('Company Age')
    plt.ylabel('Size Number')
    plt.title('Relationship between Company Age and Size Number(larger than 2000)')
    st.pyplot(plt)

def draw_skill1():
    categories = ['Python', 'Excel', 'Hadoop', 'Spark', 'AWS', 'Tableau', 'Big Data']
    values = df_skill1.sum()
    # Color settings
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#99CCFF', '#FF99CC', '#FFFF99']
    # Shadow settings
    shadow = True
    # highlight
    explode = (0.1, 0, 0, 0, 0, 0, 0)
    #clear previous residual images
    plt.clf()
    # Draw a pie chart
    plt.pie(values, labels=categories, autopct='%1.1f%%', colors=colors, shadow=shadow, explode=explode, startangle=90)
    # Add title
    plt.title('Skills Distribution')
    # Set legend
    plt.legend(loc='upper right', bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot(plt)
def draw_skill2():
    value_counts = df_skill2.value_counts()
    sns.set_style("whitegrid")

    # Create a stacked chart
    plt.figure(figsize=(10, 6))
    ax = value_counts.unstack().plot(kind='bar', stacked=True, colormap='Paired')

    # Set chart properties
    plt.title('Stacked Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Count')
    plt.xticks(rotation=90)
    plt.legend(title='add_skills')

    # Adjust legend position
    ax.legend(loc='upper right')

    # Remove top and right borders
    sns.despine()
    st.pyplot(plt)

def draw_skill3():
    python_counts = df_skill3.groupby('job_simp')['python'].sum()
    # Create a bar chart
    plt.figure(figsize=(10, 6))
    sns.barplot(x=python_counts.index, y=python_counts.values, color='skyblue')
    # Set chart properties
    plt.title('Job Demand for Python Skills')
    plt.xlabel('Job Simplified')
    plt.ylabel('Count')
    # Rotate x-axis labels to avoid overlap
    plt.xticks(rotation=0)
    st.pyplot(plt)

def draw_skill4():
    python_demand = df_skill3['python'].value_counts(normalize=True) * 100
    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(python_demand, labels=python_demand.index, autopct='%1.1f%%', startangle=90)
    # Set chart properties
    plt.title('Python Skill Demand by Job')
    plt.axis('equal')
    st.pyplot(plt)

#col1, col2,col3 = st.columns([10, 10 ,10])
#with col1:
st.subheader('This is a heat map about rating')
st.write("At first, we want to figure out which variables are closely related to rating. Then we look through the heat map, finding that the age and size of the company are highly correlated with rating, so we will first choose these three categories to study.")
draw_hot_ratingall()
#input_num = st.number_input("index",min_value=0,max_value=20)

#if input_num==1:
       # draw_hot_age_size1()
#if input_num == 2:
 #       draw_hot_age_size2()
#if input_num == 3:
 #       draw_hot_age_size3()
#if input_num==4:
  #      draw_hot_age_size4()

#with col2:
#st.write("The strong correlation between age and size is very interesting.")
#draw_size_age()
#draw_size_age2()

#with col3:
#st.write('We also noticed some data on skills. Since our major is information management, we are very interested in this.')
#draw_skill1()
#draw_skill2()
#draw_skill3()
#draw_skill4()
#st.write('This shows how important python is')
#img_url ='https://img1.baidu.com/it/u=1429673394,1784562153&fm=253&fmt=auto&app=138&f=JPEG?w=953&h=500'
#st.image(img_url, caption='python')



option = st.selectbox(":fire: Three aspects",['Rating VS age and size','age and size',"Skills"])

if option =='Rating VS age and size':
    st.header('Choose different index to observe the relationship between company age and company size and rating') # 添加标题
    
    input_num = st.number_input("index",min_value=0,max_value=4)
    if input_num==1:
        st.text('The data source for this image is the part of the company with an age of 50 ') 
        st.text('or less and a rating of 3 or more') # 添加
        progress_bar = st.progress(25) # 创建进度条对象
        draw_hot_age_size1()
    if input_num == 2:
        st.text('The data source for this image is the part of the company with an age of 50 ')
        st.text('or less and a rating of less than 3') # 添加
        progress_bar = st.progress(50) # 创建进度条对象
        draw_hot_age_size2()
    if input_num == 3:
        st.text("The data source for this image is the company's age greater than 50") 
        st.text("and rating greater than or equal to 3") # 添加
        progress_bar = st.progress(75) # 创建进度条对象
        draw_hot_age_size3()
    if input_num==4:
        st.text('The data source for this image is the part of the company that is older than 50')
        st.text('and has a rating of less than 3') # 添加
        progress_bar = st.progress(100) # 创建进度条对象
        draw_hot_age_size4()

    button_click = st.button(':sparkles: Remarks')
    if button_click:
        st.write("In the data processing of this section, we divided the company age into two parts: greater than 50 and less than 50, and the rating into two parts: greater than 3 and less than 3. This formed four different types of combinations, which are shown in the four scatter plots above")
 
        

if option == 'age and size':
    st.markdown(
        '<span style="font-size:20px;"><font color=green >*By analyzing the two plots,we found that the strong correlation between age and size is very interesting*</font></span>',     unsafe_allow_html=True)
    
    st.write("Although both of the following figures can reflect the strong correlation between Company Age and Size Number. However, the slope in the second chapter of the graph is larger than that in the first graph, and it is estimated to be two to three times larger. In other words, when the Size Number is greater than 6000, the correlation between the two becomes stronger.")
    draw_size_age()
    draw_size_age2()

    button_click = st.button(':sparkles: Remarks')
    if button_click:
        st.write('We have the following speculations about the reasons for this situation:')
        st.write('1. Long term accumulation of experience and professional knowledge')
        st.write('2. Stability and reliability')
        st.write('3. Brand influence')
        st.write('...')
        
        

if option == 'Skills':
    st.header(' Skills ') # 添加标题

    st.write('We also noticed some data on skills. Since our major is information management, we are very interested in this.')
    draw_skill1()
    st.write(':point_right: From this pie chart, we can recognize that Python has the highest contribution to data jobs, even reaching almost one-third.This number is 10% more than the contribution of Excel, which ranks second.')
    draw_skill2()
    draw_skill3()
    st.write(':point_up: From the two figures above, we understand the important position of Python in the entire data job. Now we are trying to gain a deeper understanding of the requirements for Python for various types of data jobs.')
    st.write(':point_right: As shown in this bar chart, data scientists have a huge demand for Python skills, far exceeding that of several other industries.')
    draw_skill4()
    st.write(":star: This pie chart once again proves the importance of Python in today's jobs" )
    img_url ='https://img1.baidu.com/it/u=1429673394,1784562153&fm=253&fmt=auto&app=138&f=JPEG?w=953&h=500'
    st.image(img_url, caption='python')

    
    button_click = st.button(':sparkles: Conclusion')
    if button_click:
        
        st.write('From the above data analysis, it has become one of the preferred programming languages for data scientists, data engineers, and other data workers.')
        st.write("Python's powerful libraries and frameworks provide powerful tools for data works to process, analyze, and visualize large amounts of data.In recent years, Python has also made significant contributions to the development of data visualization, with its Matplotlib library making it easy to generate high-quality data visualization. We also focused on learning how to use Python to draw charts and analyze data this semester.")
        st.write("In summary, Python plays a crucial role in the field of data science, providing researchers with powerful tools and resources to solve complex problems and drive the development of science.")


