from flask import Flask, render_template, request
import requests
from asyncio import sleep
from os import system
from fetch_members import str4nx_avatar, str4nx, hayek, hayek_avatar, mardok, mardok_avatar, nevask, nevask_avatar

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():

    return render_template('index.html', 
    hayek=hayek,
    hayek_image=hayek_avatar,

    str4nx=str4nx,
    str4nx_image=str4nx_avatar,

    mardok=mardok,
    mardok_image=mardok_avatar,

    nevask=nevask,
    nevask_image=nevask_avatar

    )

@app.route('/?id_discord=<string:nome>&submit=Enviar')

@app.route('/<string:nome>')
def error(nome):
    return f'<h1> Página "{nome}" não existe </h1>'

token = 'MTA0MzY4MDY2NDMyNDY3NzY2Mg.GfQvXd.6OAw6meOflJ6c4SjcjxWp3EYTbgRbyuDPzHz3s'

if __name__ == '__main__':
    app.run(debug=True)