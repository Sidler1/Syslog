# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import mysql.connector
import pandas.io.sql as psql

usr = "root"
pwd = "mysql"
mysqlhost = "127.0.0.1"
sql = mysql.connector.connect(host=mysqlhost, user=usr, password=pwd)
exe = sql.cursor()
sql.autocommit = True

servers = "SELECT name,ip FROM syslog_server.server where srv = '1'"
exe.execute(servers)
servers = exe.fetchall()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash("PewSysLog", external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Server auswahl', id="Pew"),
    dcc.Dropdown(
        id="serverauswahl",
        options=[{'label': server[0], 'value': server[1]} for server in servers],
        value=[],
        multi=True
    ),
    dash_table.DataTable(
        id="output-container",
        columns=[],
        style_as_list_view=True,
        style_cell={
            'whiteSpace': 'normal'
        },
        style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold'
        },
        data=[],

    )

], )


@app.callback(
    [dash.dependencies.Output('output-container', 'columns'), dash.dependencies.Output('output-container', 'data')],
    [dash.dependencies.Input('serverauswahl', 'value')])
def update_output(value_checked):
    if value_checked == "[]":
        return ""
    value_checked = str(value_checked).replace("[", "").replace("]", "").replace("'", "").replace(",", "\" OR \"")
    query = "select syslog_server.syslog_srv.tstamp as Zeit, syslog_server.syslog_srv.client_ip as Server, syslog_server.syslog_srv.service as Service, syslog_server.syslog_srv.msg as Nachricht from syslog_server.syslog_srv where client_ip = \"{}\"".format(
        value_checked)
    df = psql.read_sql(query, con=sql)
    return [{"name": i, "id": i} for i in df.columns], df.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)
