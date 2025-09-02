import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = html.Div([
    dbc.Button("💬 Open Chatbot", id="open-chat", n_clicks=0),

    dbc.Modal(
        [
            dbc.ModalHeader("Chatbot Assistant"),
            dbc.ModalBody([
                html.Div(id="chat-history", style={
                    "height": "300px", "overflowY": "auto", "border": "1px solid #ccc", "padding": "10px"
                }),
                dbc.Input(id="user-input", placeholder="Type a message...", type="text"),
                dbc.Button("Send", id="send-btn", color="primary", className="mt-2")
            ]),
        ],
        id="chat-modal",
        is_open=False,
        size="lg"
    )
])

# Callbacks
@app.callback(
    Output("chat-modal", "is_open"),
    [Input("open-chat", "n_clicks")],
    [State("chat-modal", "is_open")]
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open

# Chat handling
@app.callback(
    Output("chat-history", "children"),
    [Input("send-btn", "n_clicks")],
    [State("user-input", "value"),
     State("chat-history", "children")]
)
def update_chat(n_clicks, user_msg, history):
    if n_clicks and user_msg:
        bot_reply = f"🤖 Bot: I received '{user_msg}'"
        new_msg = [html.Div(f"👤 You: {user_msg}"), html.Div(bot_reply), html.Hr()]
        return (history or []) + new_msg
    return history

if __name__ == "__main__":
    app.run(debug=True)
