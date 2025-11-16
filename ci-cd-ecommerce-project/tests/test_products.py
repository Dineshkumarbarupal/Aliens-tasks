import pytest
from playwright.sync_api import Page, expect

@pytest.fixture
def logged_in_page(page: Page, base_url):
    """Fixture to login and return page"""
    page.goto(base_url)
    page.fill('#username', 'testuser')
    page.fill('#password', 'password')
    page.click('button:has-text("Login")')
    return page

def test_products_display(logged_in_page: Page):
    """Test products are displayed after login"""
    # Wait for products to load
    logged_in_page.wait_for_selector('.product')
    
    # Check if products are displayed
    products = logged_in_page.locator('.product')
    expect(products).to_have_count(3)
    
    # Verify product details
    expect(logged_in_page.locator('text=Laptop')).to_be_visible()
    expect(logged_in_page.locator('text=$999.99')).to_be_visible()
    expect(logged_in_page.locator('text=Smartphone')).to_be_visible()

def test_product_buy_button(logged_in_page: Page):
    """Test buy buttons are functional"""
    logged_in_page.wait_for_selector('.product')
    
    # Check buy buttons exist
    buy_buttons = logged_in_page.locator('button:has-text("Buy Now")')
    expect(buy_buttons).to_have_count(3)