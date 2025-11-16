# production_tester.py
import requests
import time
import ssl
import socket
from urllib.parse import urlparse
import pyautogui

class ProductionTester:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
    
    def run_all_tests(self):
        results = {}
        
        # Production-specific tests
        results['uptime'] = self.test_uptime()
        results['ssl_certificate'] = self.test_ssl_certificate()
        results['performance'] = self.test_performance()
        results['security_headers'] = self.test_security_headers()
        results['load_handling'] = self.test_load_handling()
        
        return results
    
    def test_uptime(self):
        try:
            response = self.session.get(self.url, timeout=10)
            return {
                'status': response.status_code == 200,
                'details': f"Status Code: {response.status_code}"
            }
        except Exception as e:
            # pyautogui.screenshot('test_uptime_error.png')
            return {'status': False, 'details': str(e)}
    
    def test_ssl_certificate(self):
        try:
            parsed_url = urlparse(self.url)
            hostname = parsed_url.hostname
            
            context = ssl.create_default_context()
            with socket.create_connection((hostname, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert()
                    
            # Check if certificate is valid
            return {
                'status': cert is not None,
                'details': "SSL Certificate is valid"
            }
        except Exception as e:
            return {'status': False, 'details': str(e)}
    
    def test_performance(self):
        try:
            start_time = time.time()
            response = self.session.get(self.url, timeout=10)
            load_time = time.time() - start_time
            
            return {
                'status': load_time < 3,  # Should load under 3 seconds
                'details': f"Page loaded in {load_time:.2f} seconds"
            }
        except Exception as e:
            return {'status': False, 'details': str(e)}
    
    def test_security_headers(self):
        try:
            response = self.session.get(self.url)
            security_headers = [
                'X-Frame-Options',
                'X-Content-Type-Options', 
                'Strict-Transport-Security',
                'Content-Security-Policy'
            ]
            
            missing_headers = []
            for header in security_headers:
                if header not in response.headers:
                    missing_headers.append(header)
            
            return {
                'status': len(missing_headers) <= 1,
                'details': f"Missing headers: {missing_headers}"
            }
        except Exception as e:
            return {'status': False, 'details': str(e)}
    
    def test_load_handling(self):
        try:
            # Simple load test - multiple rapid requests
            times = []
            for i in range(3):
                start_time = time.time()
                response = self.session.get(self.url, timeout=10)
                times.append(time.time() - start_time)
            
            avg_time = sum(times) / len(times)
            return {
                'status': avg_time < 2,
                'details': f"Average response time: {avg_time:.2f}s"
            }
        except Exception as e:
            return {'status': False, 'details': str(e)}