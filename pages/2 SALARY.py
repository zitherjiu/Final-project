import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


#Authors: Hengyi Zhang, Xinyi Huang
df = pd.read_csv("Cleaned_DS_Jobs.csv")
df_1 = df
df_2 = df_1[['max_salary', 'min_salary', 'avg_salary']]
df_3 = df_1[['job_simp', 'max_salary', 'min_salary', 'avg_salary']]
df_4 = df_3.groupby('job_simp')
df_5 = df_1[['Type of ownership', 'max_salary', 'min_salary', 'avg_salary']]
df_6 = df_5.groupby('Type of ownership')

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
dfb = dfa[dfa['job_simp'] == 'data scientist']
dfc = dfa[dfa['job_simp'] == 'analyst']
dfd = dfa[dfa['job_simp'] == 'data engineer']
dfe = dfa[dfa['job_simp'] == 'manager']
dff = dfa[dfa['job_simp'] == 'director']

# Set page title
st.title('Analysis and Display of Data Science Job Information Based on Streamlit')

# Show first-level titles
st.header('2. Analyze Salary and its Related Influencing Factors ')



import numpy as np
def draw_fir_sala():
    statistics1 = df_6.describe()
    # Extract data of maximum, minimum, mean and variance
    max_values = statistics1['max_salary']['mean'].apply(lambda x: round(x, 1))
    min_values = statistics1['min_salary']['mean'].apply(lambda x: round(x, 1))
    mean_values = statistics1['avg_salary']['std'].apply(lambda x: round(x, 1))
    # variance_values = statistics1['Mean Salary']['std'] ** 2

    plt.figure(figsize = (10,10))

    # Create a column chart
    fig, ax = plt.subplots(figsize = (10,9))
    x = range(len(df_6.groups))
    width = 0.3

    # Plot a column chart of maximum values
    ax.bar(x, max_values, width, label='Max Salary')
    # Plot a bar graph of minimum values
    ax.bar([i + width for i in x], min_values, width, label='Min Salary')
    # Plot a bar graph of the mean
    ax.bar([i + 2 * width for i in x], mean_values, width, label='Mean Salary std')

    # Show variance value
    # for i in range(len(df_4.groups)):
    #     ax.text(i, max_values[i] + 50, f'Var: {variance_values[i]:.2f}', ha='center')
    for i, v in enumerate(max_values):
        ax.text(i, v, str(v), ha='center',va='bottom' )
    for i, v in enumerate(min_values):
        ax.text(i + width, v, str(v), ha='center', va='bottom')
    for i, v in enumerate(mean_values):
        ax.text(i + 2 * width, v, str(v), ha='center', va='bottom')
    # Set abscissa label
    ax.set_xticks([i + width for i in x])
    ax.set_xticklabels(df_6.groups.keys(), rotation=0)

    # Set legends, labels, etc.
    ax.legend(loc='best')
    ax.set_xlabel('Type of Ownership')
    ax.set_ylabel('Salary')
    ax.tick_params(axis='x', rotation=90)  # Set x-axis labels to be placed horizontally
    plt.ylim((0, 250))

    # Show column chart
    plt.tight_layout()
    st.pyplot(plt)


#Authors: Hengyi Zhang, Xinyue Zhou

def draw_sec_sala():
    statistics1 = df_4.describe()
    # Extract data of maximum, minimum, mean and variance
    max_values = statistics1['max_salary']['mean'].apply(lambda x: round(x, 1))
    min_values = statistics1['min_salary']['mean'].apply(lambda x: round(x, 1))
    mean_values = statistics1['avg_salary']['std'].apply(lambda x: round(x, 1))
    # variance_values = statistics1['Mean Salary']['std'] ** 2

    plt.figure(figsize=(8, 9))

    # Create a column chart
    fig, ax = plt.subplots()
    x = range(len(df_4.groups))
    width = 0.3

    # Plot a column chart of maximum values
    ax.bar(x, max_values, width, label='Max Salary')
    # Plot a bar graph of minimum values
    ax.bar([i + width for i in x], min_values, width, label='Min Salary')
    # Plot a bar graph of the mean
    ax.bar([i + 2 * width for i in x], mean_values, width, label='Mean Salary std')

    # Show variance value
    # for i in range(len(df_4.groups)):
    #     ax.text(i, max_values[i] + 50, f'Var: {variance_values[i]:.2f}', ha='center')
    for i, v in enumerate(max_values):
        ax.text(i, v, str(v), ha='center', va='bottom')
    for i, v in enumerate(min_values):
        ax.text(i + width, v, str(v), ha='center', va='bottom')
    for i, v in enumerate(mean_values):
        ax.text(i + 2 * width, v, str(v), ha='center', va='bottom')
    # Set abscissa label
    ax.set_xticks([i + width for i in x])
    ax.set_xticklabels(df_4.groups.keys(), rotation=0)

    # Set legends, labels, etc.
    ax.legend(loc='best')
    ax.set_xlabel('Job Simplification')
    ax.set_ylabel('Salary')

    plt.ylim((0, 200))

    # Show column chart
    plt.tight_layout()
    st.pyplot(plt)



def draw_hot_all():
    df_hot = dfa[
        ['Rating', 'min_salary', 'max_salary', 'avg_salary', 'same_state', 'company_age', 'Size_num', 'if_seniority']]
    k = 7
    cols = df_hot.corr().abs().nlargest(k + 1, 'avg_salary')['avg_salary'].index
    cm = df_hot[cols].corr()
    plt.figure(figsize=(8, 5))
    plt.title('All')
    sns.heatmap(cm, annot=True, cmap='Blues')
    st.pyplot(plt)


def draw_hot_sci():
    # Analyze with data science
    df_hot = dfb[
        ['Rating', 'min_salary', 'max_salary', 'avg_salary', 'same_state', 'company_age', 'Size_num', 'if_seniority']]
    k = 7
    cols = df_hot.corr().abs().nlargest(k + 1, 'avg_salary')['avg_salary'].index
    cm = df_hot[cols].corr()
    plt.figure(figsize=(8, 5))
    plt.title('Data Scientist')
    sns.heatmap(cm, annot=True, cmap='Blues')
    st.pyplot(plt)

def draw_hot_analy():
    df_hot = dfc[
        ['Rating', 'min_salary', 'max_salary', 'avg_salary', 'same_state', 'company_age', 'Size_num', 'if_seniority']]
    k = 7
    cols = df_hot.corr().abs().nlargest(k + 1, 'avg_salary')['avg_salary'].index
    cm = df_hot[cols].corr()
    plt.figure(figsize=(8, 5))
    plt.title('Analyst')
    sns.heatmap(cm, annot=True, cmap='Blues')
    st.pyplot(plt)

def draw_hot_engineer():
    df_hot = dfd[
        ['Rating', 'min_salary', 'max_salary', 'avg_salary', 'same_state', 'company_age', 'Size_num', 'if_seniority']]
    k = 7
    cols = df_hot.corr().abs().nlargest(k + 1, 'avg_salary')['avg_salary'].index
    cm = df_hot[cols].corr()
    plt.figure(figsize=(8, 5))
    plt.title('Data Engineer')
    sns.heatmap(cm, annot=True, cmap='Blues')
    st.pyplot(plt)






#Authors: Hengyi Zhang, Yujia Liao
st.subheader('(1) Two Bar Charts to See the Salary Situation')
#st.write('This is about salary')

draw_fir_sala()
st.write("This graph reflects the distribution of wage levels for different types of ownership. Obviously, the highest salary at Hospital is much higher than that of other types. Meanwhile, the highest salary values for other types of ownership are relatively similar. For the Hospital, the numerical difference between the highest and lowest salaries is also the largest. Furthermore, the salary values of other organization and self employed are concentrated, with small deviations and relatively stable salary levels.")
 

draw_sec_sala()

on = st.toggle('Remarks')
if on:
    st.write(":point_right: From this image, it is not difficult to see that from the perspective of the highest or lowest wage level, the overall salary level of the manager is the highest.But the manager's STD is also relatively highest. This indicates that the salary distribution of managers at different levels is relatively more dispersed, with significant numerical differences.On the contrary, the distribution of wage values for engineers in different levels is the most concentrated. This indicates that for engineers of different levels, the wage gap is relatively small." )


st.subheader('(2) Two Heatmaps to Study the Correlation between Salary and Other Variables')


draw_hot_all()
on = st.toggle('Some pity in cleaning the data')
if on:
    st.write('At first, we hoped to find variables such as company age and whether they were in the same state to find a correlation between them and wages, but the heat map obtained showed that their correlation was weak. So we decided to find whether there were any correlation between different ownerships and salary.')

#Propose relevant information only for the top 4 companies in terms of quantity
desired_ownership = ['Company - Private', 'Company - Public', 'Nonprofit Organization', 'Subsidiary or Business Segment']
dfa = df[df['Type of ownership'].isin(desired_ownership)]

#Separate 4 companies
ownership_dummies = pd.get_dummies(dfa['Type of ownership'], prefix="for_", drop_first=False, dtype = int)
#set up at the end of the table on the right side of dfb
dfb = dfa.join(ownership_dummies)

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
    

dfb['Size_num'] = dfb['Size'].apply(get_sizenum)



k = 7 #number of variables for heatmap
## Get the k most correlated in absolute value
## Since obviously the outcome is perfectly correlated with itself
var_of_interest = 'avg_salary'
df_11 = dfb[['Rating', 'company_age','Size_num','avg_salary']+ ownership_dummies.columns.tolist()]
cols = df_11.corr().abs().nlargest(k+1, var_of_interest)[var_of_interest].index
cm = df_11[cols].corr()
plt.figure(figsize=(10,6))
sns.heatmap(cm, annot=True, cmap = 'Blues');
plt.title("Data Scientist only" , fontsize = 20)
st.pyplot(plt)


on = st.toggle('Conclusion')
if on:
    st.write('Since the number of data scientists is the highest among job types, we chose to conduct correlation analysis on this job type. We also used the same principle to select the four types of companies with the highest number. By plotting the heat map, we can find that the correlation between variables and average salaries has been significantly enhanced compared to the first processing method ')
#st.write('From several scattered heat maps, wages can be analyzed from four factors，age，rating，size，state')

