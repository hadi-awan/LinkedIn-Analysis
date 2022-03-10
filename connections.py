# Import Libraries and Datasets
import plotly.express as px
import pandas as pd


lkd = pd.read_csv('Connections.csv')

lkd = lkd.sort_values(by='Connected On')

# Timeline: How is my Connection activity overtime?
fig_1 = px.line(data_frame=lkd.groupby(by='Connected On').count().reset_index(),
                x='Connected On',
                y='First Name',
                labels={'First Name': 'Number of Connections'},
                title='Connection Timeline')
fig_1.show()

# Where do my connections work?
group_company = lkd.groupby(by='Company').count().reset_index()

group_company = group_company.sort_values(by='Company', ascending=False).reset_index(drop=True)

fig_2 = px.bar(group_company[:200],
               x='Company',
               y='Connected On',
               labels={'Connected On': 'Number of Connections'},
               width=1000,
               height=900,
               title='Bar graph for companies that my Connections are working at.')
fig_2.show()


# Which positions do my connections hold?
fig_3 = px.bar(data_frame=lkd.groupby(by='Position').count().sort_values(by='First Name', ascending=False).reset_index(),
               x='Position',
               y='Connected On',
               labels={'Connected On': 'Number of Connections'},
               title='The various Positions occupied by my Connections')
fig_3.show()

