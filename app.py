import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv('tweet_ana.csv')
with open('Tweet_topic_sentiment.json','r') as f:
         data = json.load(f)
sa2 = '206041122'

#app.layout = html.Div([
    # 横向柱形图
dcc.Graph(
    className='city_graph',
    figure=go.Figure(
        data = [go.bar(
            x = list(data[sa2]['hashtag'].values())[:10][::-1],
            y = list(data[sa2]['hashtag'].keys())[:10][::-1]
            #type =  'bar'
            )],
        layout=go.layout(
            orientation= 'h',
            ylabel='hashtags',
            xlabel= 'frequency',
            title=data[sa2]['sa2_name']+'\'s hot topics on Social Media',
            showlegend = True,
            legend = go.layout.Legend(x=0,y=1.0),
            yaxis = go.yaxis(hoverformat='.0f'),
            margin=go.layout.Margin(l = 80, r= 35, t=50, b=30)
        )),
    id='graph-bar-horizontal',
    style={'height':300}
)
    #])


if __name__ == '__main__':
    app.run_server(debug=True, port=8053, dev_tools_hot_reload=False, use_reloader=False)
