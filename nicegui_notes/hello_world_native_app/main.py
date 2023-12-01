from nicegui import native, ui

ui.label('Hello NiceGUI!')

ui.run(title='hello_world_native_app', native=True, reload=False, port=native.find_open_port())
