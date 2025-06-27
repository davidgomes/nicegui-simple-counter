from nicegui import ui, app

def create():
    @ui.page('/')
    def counter_page():
        # Initialize counter value in user storage to persist across sessions
        if 'counter_value' not in app.storage.user:
            app.storage.user['counter_value'] = 0
        
        # Create UI elements
        with ui.column().classes('items-center gap-4 p-8'):
            ui.label('Simple Counter').classes('text-2xl font-bold')
            
            # Counter display with large, prominent styling
            counter_display = ui.label().classes('text-6xl font-mono text-primary')
            
            # Increment button
            increment_btn = ui.button('Increment', icon='add').classes('text-lg px-6 py-3')
            
            # Reset button (smaller, secondary style)
            reset_btn = ui.button('Reset', icon='refresh', color='grey').classes('mt-4')
        
        def update_display():
            counter_display.text = str(app.storage.user['counter_value'])
        
        def increment_counter():
            app.storage.user['counter_value'] += 1
            update_display()
            # Visual feedback
            ui.notify(f'Counter: {app.storage.user["counter_value"]}', type='positive', position='top')
        
        def reset_counter():
            app.storage.user['counter_value'] = 0
            update_display()
            ui.notify('Counter reset!', type='info', position='top')
        
        # Set up event handlers
        increment_btn.on_click(increment_counter)
        reset_btn.on_click(reset_counter)
        
        # Initialize display
        update_display()