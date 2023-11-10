import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np




df = pd.read_csv("D:\MISY\Homework\Assignment\\Cleaned_DS_Jobs.csv")



# 设置网页标题
st.title('Analysis and Display of Data Science Job Information Based on Streamlit')
# 展示一级标题
st.header('1. Analysis of Different Job Types and Different Onerships in Data Science ')


groups_job_simp = df['job_simp'].sort_values().unique().tolist()# job_simp和job_title 的种类
groups_title = df['Job Title'].sort_values().unique().tolist()

df1 = df[['job_simp', 'Job Title']]# 创建新的df1,只包含两列

df1 = df1.groupby('job_simp') # 第一列七种job, 第二列是每种job对应的职位

df1.value_counts() # 合计职位数

df1 = df[['job_simp']]
# df1= df1.groupby('job_simp')
counts1 = df1.value_counts() # 合计job种类数——7个

df11 = df[['job_simp', 'Type of ownership', 'company_age', 'seniority']]
# 对上述的几个因素进行一些细分析

df12 = df11[['job_simp', 'Type of ownership']]
df12 = df12[df12['Type of ownership']!='-1']

# 设置plt类型
plt.style.use("seaborn-v0_8")



## JOB TYPES
def draw_job():
    fig, ax1 = plt.subplots(1, figsize=(12, 6))

    # 统计工作类型的数量
    job_counts = df12['job_simp'].value_counts()

    # 绘制工作类型的数量图
    job_counts.plot(kind='bar', ax=ax1)
    ax1.set_title('Job Type Counts', fontsize=20,color = "blue")
    ax1.set_xlabel('Job Type', fontsize=15)
    ax1.set_ylabel('Count', fontsize=15)
    ax1.tick_params(axis='x', rotation=90)  # 设置 x 轴标签水平放置
    st.pyplot(fig)

def draw_Company():
    fig, ax2 = plt.subplots(1, figsize=(12, 6))   
    # 统计企业类型的数量

    ownership_counts = df12['Type of ownership'].value_counts()

    # 绘制企业类型的数量图
    ownership_counts.plot(kind='bar', ax=ax2)
    ax2.set_title('Ownership Type Counts', fontsize=20, color = "blue")
    ax2.set_xlabel('Ownership Type', fontsize=15)
    ax2.set_ylabel('Count')
    ax2.tick_params(axis='x', rotation=90)  # 设置 x 轴标签水平放置

    st.pyplot(fig)
def draw_age():
    # 创建子图
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    # 绘制第一个图表 - 公司年龄小于30的计数
    df_ages = df['company_age']
    value_counts = df_ages.value_counts()
    filtered_counts = value_counts[value_counts.index < 30]
    sorted_counts = filtered_counts.sort_index()
    axes[0].plot(sorted_counts.index, sorted_counts.values)
    axes[0].set_title('Value Counts of Company Age (Age < 30)',fontsize=20, color = "blue")
    axes[0].set_xlabel('Company Age')
    axes[0].set_ylabel('Count')
    # 绘制第二个图表 - 公司年龄大于30的计数
    filtered_counts = value_counts[value_counts.index > 30]
    sorted_counts = filtered_counts.sort_index()
    axes[1].plot(sorted_counts.index, sorted_counts.values)
    axes[1].set_title('Value Counts of Company Age (Age > 30)',fontsize=20, color = "blue")
    axes[1].set_xlabel('Company Age')
    axes[1].set_ylabel('Count')
    # 调整子图之间的间距
    plt.tight_layout()
    # 显示图表
    st.pyplot(fig)



def draw_combine1():
    fig, ax2 = plt.subplots(1, figsize=(10, 10))
    fig.subplots_adjust(wspace=1)
    # 绘制第二个图表
    counts = df12.value_counts()
    counts.plot(kind='barh', ax=ax2)
    ax2.set_title('Job Type and Ownership Type Counts',fontsize=20)
    ax2.set_xlabel('Count')
    ax2.set_ylabel('Job Type, Ownership Type')
    # 显示图表
    st.pyplot(fig)

def draw_combine2():
    # 创建Figure对象和子图
    fig, ax1 = plt.subplots(1, figsize=(14, 10))
    fig.subplots_adjust(wspace=1)
    # 绘制第一个图表
    grouped = df12.groupby(['job_simp', 'Type of ownership']).size().unstack()
    grouped.plot(kind='bar', stacked=True, ax=ax1)
    ax1.set_title('Job Type by Ownership Type',fontsize=25)
    ax1.set_xlabel('Job Type')
    ax1.set_ylabel('Count')
    ax1.legend(loc='upper right')
    # 显示图表
    st.pyplot(fig)

def draw_combine3():
    fig, ax = plt.subplots(figsize=(8, 6))

    # 过滤无效的公司年龄数据
    df14 = df11[['job_simp', 'company_age']]
    df14 = df14[df14['company_age'] != '-1']

    # 提取工作类型和公司年龄数据
    job_types = df14['job_simp']
    company_age = df14['company_age'].astype(int)

    # 创建DataFrame，包含工作类型和公司年龄数据
    data = pd.DataFrame({'Job Type': job_types, 'Company Age': company_age})

    # 使用Seaborn的stripplot绘制比率图
    sns.stripplot(x='Company Age', y='Job Type', data=data, ax=ax, jitter=True, palette='Set2')

    # 设置图表标题和轴标签
    ax.set_title('Job Type by Company Age',fontsize=20)
    ax.set_xlabel('Company Age')
    ax.set_ylabel('Job Type')

    # 调整子图之间的间距
    plt.tight_layout()

    # 显示图表
    st.pyplot(fig)



option = st.selectbox(":fire: Three aspects ",['Job Types','Company Types',"Combination"])
if option =='Job Types':
    st.header(" Here we show different Jobs' situation") # 添加标题
    draw_job()
    st.write("  :point_right:  From the obtained bar chart we can find that in the sample data, the proportion of data scientists is the highest, with a count of 400, when the number of directors is the lowest, and the proportion of na, analysts, data engineers, and mle is close and in the middle.") # 添加评论

    st.header(' Pictures of different job types ')
    st.write(':point_down: Here are some representative image of different types of work')
    col1, col2, col3,col4 = st.columns([10, 10,10,10]) # 把图片按列横向排版

    with col1:
        st.text("Mle")
        st.image('https://img2.baidu.com/it/u=2526428600,466199796&fm=253&fmt=auto&app=120&f=JPEG?w=1138&h=641',use_column_width=True)

    with col2:
        st.text("Data Engineer")
        st.image('https://img0.baidu.com/it/u=2931491258,609966211&fm=253&fmt=auto&app=138&f=JPEG?w=605&h=500',use_column_width=True)
    with col3:
        st.text("Data Scientist")
        st.image('https://img0.baidu.com/it/u=2703552960,1537318359&fm=253&fmt=auto&app=138&f=JPEG?w=750&h=500',use_column_width=True)
    with col4:
        st.text("Director")
        st.image('http://t13.baidu.com/it/u=1989827379,4287581357&fm=224&app=112&f=JPEG?w=500&h=500',use_column_width=True)
    
    col5, col6, col7=st.columns([10, 10,10])

    with col5:
        st.text("Manager")
        st.image('https://img1.baidu.com/it/u=2745896578,1399083701&fm=253&fmt=auto&app=138&f=JPEG?w=702&h=500',use_column_width=True)
    with col6:
        st.text("Analyst")
        st.image('http://t14.baidu.com/it/u=3821843656,496867567&fm=224&app=112&f=JPEG?w=500&h=500',use_column_width=True)

    with col7:
        st.text("Na")
        st.image('https://img0.baidu.com/it/u=1689116355,3364441922&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500',use_column_width=True)
    
 
        
if option == 'Company Types':
    st.markdown(
        '<span style="font-size:20px;"><font color=green >*Through analyzing the data samples, we found that private companies account for the largest proportion, with a total of nearly 400 companies. Similar to this are public companies, with a total of 150. The number of other types of companies is relatively small, with less than 50 companies in total.*</font></span>',     unsafe_allow_html=True)
    draw_Company()
    
    st.header('Company age statistics')
    draw_age()
    button_click = st.button(':sparkles: Analysis of company age data')
    if button_click:
        st.write('In processing data on the age group of companies, we divide them into two categories: those over 30 years old and those under 30 years old. In terms of the total number, most companies are under 30 years, when the number of companies with an age of 0 being the highest, reaching nearly 120. The proportion of companies aged over 30 years in the total is relatively small and evenly distributed.')
        



if option == 'Combination':
    st.header(' Ownership ') # 添加标题

    draw_combine1()
    st.write(':point_right: From this graph,obviously, we can see that the number of data scientists is far greater than the number of other jobs types. For data scientists, private companys are nearly three times as many as public companys. Furthermore, the number of job types such as na, data engineer, and analyst is relatively similar, all of which are less than one-fifth that of data scientists. The number of professions such as manager and director is very small.')
    draw_combine2()
    st.write(':point_right: This bar chart more intuitively shows the proportion of different ownership in each different jobs. Overall, private companies account for over half of every profession. But for the director, the vast majority of ownership is owned by public companies.')
    
    st.header(' Age ') # 添加标题
    draw_combine3()
    button_click = st.button(':sparkles: Conclusion')
    if button_click:
        st.write('This scatter plot mainly reflects the approximate relationship between company age and job type. It is obvious that these professions are relatively emerging, so they are mainly concentrated in companies under the age of 50. Among them, data scientist shows the most obvious performance. The younger the company, the newer the company, and the higher their professional demand for data scientists. In other words, in recent years, there has been a significant demand for data scientist positions in newly established companies.')



