# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import mysql.connector
import pandas.io.sql as psql

usr = "felix"
pwd = "mysql"
mysqlhost = "192.168.0.234"
sql = mysql.connector.connect(host=mysqlhost, user=usr, password=pwd)
exe = sql.cursor()
sql.autocommit = True

servers = "SELECT name,ip FROM syslog_server.server where srv = '1'"
exe.execute(servers)
servers = exe.fetchall()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash("PewSysLog", external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Dropdown(
        id="serverauswahl",
        options=[{'label': server[0], 'value': server[1]} for server in servers],
        value=[],
        multi=True
    ),
    dcc.Dropdown(
        id="klasse",
        options=[{'label': 'Server', 'value': 'syslog_server.syslog_srv'}],
        value="syslog_server.syslog_srv",
    ),
    html.Div(
        dash_table.DataTable(
            id="output-container",
            columns=[],
            style_cell={
                'whiteSpace': 'normal',
                'textAlign': 'left'
            },
            style_header={
                'backgroundColor': 'white',
                'fontWeight': 'bold'
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)',
                }
            ],
            sort_action='custom',
            sort_mode='single',
            data=[]
        )
    )
])


@app.callback(
    [dash.dependencies.Output('output-container', 'columns'), dash.dependencies.Output('output-container', 'data')],
    [dash.dependencies.Input('serverauswahl', 'value'), dash.dependencies.Input('klasse', 'value')])
def update_output(val_server, val_klasse):
    if not val_server:
        query = "select {0}.tstamp as Zeit, {0}.client_ip as Server, {0}.service as Service, {0}.msg as Nachricht from {0}".format(
            val_klasse)
        df = psql.read_sql(query, con=sql)
        return [{"name": i, "id": i} for i in df.columns], df.to_dict('records')
    val_server = str(val_server).replace("[", "").replace("]", "").replace("'", "").replace(",", "\" OR \"")
    query = "select {0}.tstamp as Zeit, {0}.client_ip as Server, {0}.service as Service, {0}.msg as Nachricht from {0} where {0}.client_ip = \"{1}\"".format(
        val_klasse, val_server)
    df = psql.read_sql(query, con=sql)
    return [{"name": i, "id": i} for i in df.columns], df.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)
