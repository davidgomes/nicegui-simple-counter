from nicegui import ui, app

def create():
    @ui.page('/')
    def counter_page():
        # Add custom CSS for pink theme
        ui.add_head_html('''
        <style>
            :root {
                --q-primary: #ec4899 !important;
                --q-secondary: #f9a8d4 !important;
                --q-accent: #fce7f3 !important;
            }
            
            .pink-gradient {
                background: linear-gradient(135deg, #fce7f3 0%, #f9a8d4 50%, #ec4899 100%);
                min-height: 100vh;
            }
            
            .pink-card {
                background: rgba(255, 255, 255, 0.9);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(236, 72, 153, 0.2);
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(236, 72, 153, 0.15);
            }
            
            .pink-counter {
                background: linear-gradient(45deg, #ec4899, #f472b6);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                text-shadow: 0 2px 4px rgba(236, 72, 153, 0.2);
            }
            
            .pink-button {
                background: linear-gradient(135deg, #ec4899, #f472b6) !important;
                border: none !important;
                box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3) !important;
                transition: all 0.3s ease !important;
            }
            
            .pink-button:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 6px 20px rgba(236, 72, 153, 0.4) !important;
            }
            
            .pink-reset {
                background: linear-gradient(135deg, #f9a8d4, #fce7f3) !important;
                color: #ec4899 !important;
                border: 2px solid #ec4899 !important;
            }
            
            .pink-reset:hover {
                background: linear-gradient(135deg, #fce7f3, #f9a8d4) !important;
                transform: translateY(-1px) !important;
            }
        </style>
        ''')
        
        # Initialize counter value in user storage to persist across sessions
        if 'counter_value' not in app.storage.user:
            app.storage.user['counter_value'] = 0
        
        # Create main container with pink gradient background
        with ui.column().classes('pink-gradient w-full items-center justify-center'):
            # Main card container
            with ui.card().classes('pink-card p-8 m-4 items-center gap-6'):
                # Title with pink styling
                ui.label('💖 Pink Counter 💖').classes('text-3xl font-bold').style('color: #ec4899')
                
                # Counter display with pink gradient text
                counter_display = ui.label().classes('text-7xl font-mono pink-counter font-bold')
                
                # Button container
                with ui.row().classes('gap-4 items-center'):
                    # Increment button with pink theme
                    increment_btn = ui.button('✨ Increment', icon='add').classes('pink-button text-lg px-8 py-4 text-white font-semibold rounded-full')
                    
                    # Reset button with pink outline style
                    reset_btn = ui.button('🔄 Reset', icon='refresh').classes('pink-reset text-lg px-6 py-3 font-semibold rounded-full')
                
                # Decorative elements
                ui.label('Click the button to increment your pink counter!').classes('text-sm opacity-70').style('color: #ec4899')
        
        def update_display():
            counter_display.text = str(app.storage.user['counter_value'])
        
        def increment_counter():
            app.storage.user['counter_value'] += 1
            update_display()
            # Pink-themed notification
            ui.notify(f'💖 Counter: {app.storage.user["counter_value"]} 💖', 
                     type='positive', position='top', color='pink')
        
        def reset_counter():
            app.storage.user['counter_value'] = 0
            update_display()
            ui.notify('✨ Counter reset! Ready for more pink magic! ✨', 
                     type='info', position='top', color='pink')
        
        # Set up event handlers
        increment_btn.on_click(increment_counter)
        reset_btn.on_click(reset_counter)
        
        # Initialize display
        update_display()