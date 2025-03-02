#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


pip install matplotlib


# In[4]:


pip install seaborn


# In[5]:


import matplotlib.pyplot as plt


# In[6]:


import seaborn as sns


# In[7]:


df = pd.read_csv('Customer Churn.csv')
df


# In[8]:


df = pd.read_csv('Customer Churn.csv')


# In[9]:


df = pd.read_csv("C:\Users\PIYUSH\Downloads\Customer Churn.csv")


# In[10]:


df = pd.read_csv("C:\\Users\\PIYUSH\\Downloads\\Customer Churn.csv")


# In[11]:


df


# In[12]:


df.head()


# In[13]:


df.info()


# In[15]:


df["TotalCharges"] = df["TotalCharges"].replace(" ","0")
df["TotalCharges"] = df["TotalCharges"].astype("float")


# In[16]:


df.info()


# In[20]:


df.isnull().sum().sum()


# In[21]:


df.describe()


# In[23]:


df.duplicated().sum()


# In[24]:


df["customerID"].duplicated().sum()


# In[26]:


def conv(value):
    if value == 1:
        return "yes"
    else:
        return "no"
    
df['SeniorCitizen'] = df["SeniorCitizen"].apply(conv)


# In[27]:


df.head()


# In[28]:


df.head(10)


# In[29]:


df.head(20)


# In[30]:


df.head(30)


# In[32]:


sns.countplot(x = 'Churn', data = df)
plt.show()


# In[40]:


ax = sns.countplot(x = 'Churn', data = df)
ax.bar_label(ax.containers[0])
plt.title("Count of customers by Churn")
plt.show()


# In[35]:


gb = df.groupby("Churn").agg({'Churn':"count"})
gb


# In[41]:


plt.figure(figsize = (3,4))
gb = df.groupby("Churn").agg({'Churn':"count"})
plt.pie(gb['Churn'], labels = gb.index, autopct = "%1.2f%%")
plt.title("Percentage of Churned Customers")
plt.show()
gb


# In[47]:


sns.countplot(x = "gender", data = df, hue = "Churn")
plt.title("Churn By Gender")
plt.show()


# In[52]:


ax = sns.countplot(x = "SeniorCitizen", data = df)
ax.bar_label(ax.containers[0])
plt.title("Count of Customers By Senior Citizen")
plt.show()


# In[50]:


counts = df.groupby(["SeniorCitizen", "Churn"]).size().unstack()

# Convert to percentages
percentages = counts.div(counts.sum(axis=1), axis=0) * 100

# Plot stacked bar chart
ax = percentages.plot(kind="bar", stacked=True, colormap="viridis", figsize=(8,6))

# Add labels (percentages)
for bars in ax.containers:
    ax.bar_label(bars, fmt="%.1f%%", label_type="center", color="white", fontsize=12)

plt.title("Churn by SeniorCitizen (Stacked Bar with Percentage)")
plt.xlabel("SeniorCitizen")
plt.ylabel("Percentage")
plt.legend(title="Churn")
plt.xticks(rotation=0)
plt.show()


# In[51]:


counts = df.groupby(["gender", "Churn"]).size().unstack()

# Convert to percentages
percentages = counts.div(counts.sum(axis=1), axis=0) * 100

# Plot stacked bar chart
ax = percentages.plot(kind="bar", stacked=True, colormap="viridis", figsize=(8,6))

# Add labels (percentages)
for bars in ax.containers:
    ax.bar_label(bars, fmt="%.1f%%", label_type="center", color="white", fontsize=12)

plt.title("Churn by Gender (Stacked Bar with Percentage)")
plt.xlabel("Gender")
plt.ylabel("Percentage")
plt.legend(title="Churn")
plt.xticks(rotation=0)
plt.show()


# In[56]:


plt.figure(figsize = (9,4))
sns.histplot(x = "tenure", data = df, bins = 72, hue = "Churn")
plt.show()


# In[59]:


ax = sns.countplot(x = "Contract", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
plt.title("Count Of Customers By Contract")
plt.show()


# In[61]:


df.columns.values


# In[67]:


columns = ['PhoneService', 'MultipleLines', 'InternetService',
           'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
           'TechSupport', 'StreamingTV', 'StreamingMovies']

# Set up the figure and axes
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 12))  # 3x3 grid of subplots
fig.suptitle("Count Plots for Various Services", fontsize=16)

# Flatten axes array for easy iteration
axes = axes.flatten()

# Generate count plots for each column
for i, col in enumerate(columns):
    sns.countplot(x=df[col], hue=df["Churn"], ax=axes[i], palette="viridis")
    axes[i].set_title(f"Distribution of {col}")
    axes[i].set_xlabel("")
    axes[i].set_ylabel("Count")
    axes[i].tick_params(axis='x', rotation=45)  # Rotate x-axis labels if needed

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Leave space for the main title
plt.show()


# In[76]:


plt.figure(figsize = (10,4))
ax = sns.countplot(x = "PaymentMethod", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
plt.title("Churned Customers By Payment Method")
plt.show()


# In[ ]:




