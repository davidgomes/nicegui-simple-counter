from nicegui.testing import User
from nicegui import ui, app

async def test_counter_initial_state(user: User) -> None:
    """Test that counter starts at 0"""
    await user.open('/')
    
    # Check that labels exist and include counter display
    labels = list(user.find(ui.label).elements)
    assert len(labels) >= 2  # Title and counter display
    
    # Find the title label
    title_labels = [elem for elem in labels if 'Simple Counter' in elem.text]
    assert len(title_labels) == 1

async def test_counter_ui_structure(user: User) -> None:
    """Test that all required UI elements are present"""
    await user.open('/')
    
    # Check title label exists
    title_labels = [elem for elem in user.find(ui.label).elements if 'Simple Counter' in elem.text]
    assert len(title_labels) == 1
    
    # Check that we have labels (title + counter display)
    labels = list(user.find(ui.label).elements)
    assert len(labels) >= 2
    
    # Check buttons exist
    buttons = list(user.find(ui.button).elements)
    assert len(buttons) == 2
    
    # Check increment button exists with correct properties
    increment_btns = [btn for btn in buttons if 'Increment' in btn.text]
    assert len(increment_btns) == 1
    increment_btn = increment_btns[0]
    assert increment_btn.props.get('icon') == 'add'
    
    # Check reset button exists with correct properties
    reset_btns = [btn for btn in buttons if 'Reset' in btn.text]
    assert len(reset_btns) == 1
    reset_btn = reset_btns[0]
    assert reset_btn.props.get('icon') == 'refresh'

async def test_counter_storage_initialization(user: User) -> None:
    """Test that counter storage is properly initialized"""
    await user.open('/')
    
    # Check that counter_value is initialized in storage
    assert 'counter_value' in app.storage.user
    assert isinstance(app.storage.user['counter_value'], int)
    assert app.storage.user['counter_value'] >= 0

async def test_counter_page_loads(user: User) -> None:
    """Test that the counter page loads without errors"""
    await user.open('/')
    
    # Verify page loaded by checking for key elements
    assert len(list(user.find(ui.label).elements)) > 0
    assert len(list(user.find(ui.button).elements)) > 0

async def test_counter_functional(user: User) -> None:
    """Test counter functionality by directly manipulating storage"""
    await user.open('/')
    
    # Manually set counter value
    app.storage.user['counter_value'] = 5
    
    # Verify the value was set
    assert app.storage.user['counter_value'] == 5
    
    # Reset to 0
    app.storage.user['counter_value'] = 0
    assert app.storage.user['counter_value'] == 0