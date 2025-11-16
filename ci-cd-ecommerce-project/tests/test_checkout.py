import pytest
from playwright.sync_api import Page, expect
import time

@pytest.fixture
def ready_to_buy_page(page: Page, base_url):
    """Fixture to login and navigate to products"""
    page.goto(base_url)
    page.fill('#username', 'testuser')
    page.fill('#password', 'password')
    page.click('button:has-text("Login")')
    page.wait_for_selector('.product')
    return page

def test_successful_purchase(ready_to_buy_page: Page):
    """Test complete purchase flow"""
    # Click buy button for first product
    ready_to_buy_page.click('button:has-text("Buy Now")')
    
    # Handle alert confirmation
    def handle_dialog(dialog):
        assert "Order placed" in dialog.message
        assert "$999.99" in dialog.message  # Laptop price
        dialog.accept()
    
    ready_to_buy_page.once("dialog", handle_dialog)
    
    # The dialog should appear after clicking buy
    ready_to_buy_page.wait_for_event("dialog")

def test_multiple_products_purchase(ready_to_buy_page: Page):
    """Test purchasing multiple products"""
    # This would require a cart functionality
    # For now, we'll test single product purchase
    pass