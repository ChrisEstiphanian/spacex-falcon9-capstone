# SpaceX Launch Records Dashboard (Plotly Dash)
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

spacex_df = pd.read_csv(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

app = dash.Dash(__name__)

site_options = [{'label': 'All Sites', 'value': 'ALL'}] + [
    {'label': s, 'value': s} for s in sorted(spacex_df['Launch Site'].unique())]

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    # TASK 1: Launch site dropdown
    dcc.Dropdown(id='site-dropdown', options=site_options, value='ALL',
                 placeholder='Select a Launch Site here', searchable=True),
    html.Br(),
    # TASK 2: Pie chart of successful launches
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),
    html.P("Payload range (Kg):"),
    # TASK 3: Payload range slider
    dcc.RangeSlider(id='payload-slider', min=0, max=10000, step=1000,
                    marks={i: str(i) for i in range(0, 10001, 2500)},
                    value=[min_payload, max_payload]),
    # TASK 4: Scatter chart of payload vs. outcome
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


# TASK 2 callback: pie chart
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        data = spacex_df.groupby('Launch Site', as_index=False)['class'].sum()
        return px.pie(data, values='class', names='Launch Site',
                      title='Total Successful Launches by Site')
    filtered = spacex_df[spacex_df['Launch Site'] == entered_site]
    counts = filtered['class'].value_counts().rename(index={1: 'Success', 0: 'Failure'}).reset_index()
    counts.columns = ['Outcome', 'Count']
    return px.pie(counts, values='Count', names='Outcome',
                  title=f'Total Launch Outcomes for Site {entered_site}',
                  color='Outcome', color_discrete_map={'Success': '#2ca02c', 'Failure': '#d62728'})


# TASK 4 callback: scatter chart
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value')])
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)]
    title = 'Correlation between Payload and Success for All Sites'
    if entered_site != 'ALL':
        df = df[df['Launch Site'] == entered_site]
        title = f'Correlation between Payload and Success for {entered_site}'
    return px.scatter(df, x='Payload Mass (kg)', y='class', color='Booster Version Category', title=title)


if __name__ == '__main__':
    app.run(debug=False)
