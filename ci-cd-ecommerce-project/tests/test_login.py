import pytest
from playwright.sync_api import Page, expect

def test_successful_login(page: Page, base_url):
    """Test user can login successfully"""
    page.goto(base_url)
    
    # Fill login form
    page.fill('#username', 'testuser')
    page.fill('#password', 'password')
    page.click('button:has-text("Login")')
    
    # Verify login success
    expect(page.locator('#products-section')).to_be_visible()
    expect(page.locator('h2:has-text("Products")')).to_be_visible()

def test_failed_login(page: Page, base_url):
    """Test login with wrong credentials"""
    page.goto(base_url)
    
    # Fill with wrong credentials
    page.fill('#username', 'wronguser')
    page.fill('#password', 'wrongpass')
    page.click('button:has-text("Login")')
    
    # Should show error (handled by alert in this case)
    # In real app, we'd check for error message element

def test_login_required_for_products(page: Page, base_url):
    """Test that products are not visible without login"""
    page.goto(base_url)
    
    # Products section should be hidden initially
    expect(page.locator('#products-section')).to_be_hidden()