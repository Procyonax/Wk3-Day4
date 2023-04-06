from app import app
from flask import render_template, url_for, request, redirect
from models.event_list import events, find_event_by_id, add_new_event
from models.event import Event

@app.route('/')
def index():
    return redirect(url_for('all_events'))

@app.route('/events')
def all_events():
    return render_template('index.html', title='Home', event_list=events)

@app.route('/events/<int:event_id>')
def show_event(event_id):
    event = find_event_by_id(event_id)
    return render_template('show.html', title='Event', event=event)

@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['event']
    event_date = request.form['date']
    event_guests = request.form['guests']
    event_room = request.form['room']
    event_description = request.form['description']
    recurring = True if 'recurring' in request.form else False
    new_id = len(events) + 1
    new_event = Event(new_id, event_name, event_date, event_guests, event_room, event_description, recurring)
    add_new_event(new_event)


    return render_template('index.html', title='events', event_list=events)