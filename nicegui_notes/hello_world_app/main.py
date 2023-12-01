from nicegui import native, ui

ui.label('Hello NiceGUI!')

ui.run(title='hello_world_app', reload=False, port=native.find_open_port())
