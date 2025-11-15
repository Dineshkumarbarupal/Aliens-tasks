import tkinter as tk
from tkinter import ttk, messagebox
import threading
from development_tester import DevelopmentTester
from production_tester import ProductionTester

class WebsiteTester:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Website Testing Tool")
        self.root.geometry("600x400")
        
        self.create_gui()
    
    def create_gui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = ttk.Label(main_frame, text="Website Testing Tool", 
                         font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # URL Input
        url_frame = ttk.Frame(main_frame)
        url_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(url_frame, text="Website URL:").pack(side=tk.LEFT)
        self.url_entry = ttk.Entry(url_frame, width=50)
        self.url_entry.pack(side=tk.LEFT, padx=10)
        self.url_entry.insert(0, "https://www.google.com")
        
        # Testing Options Frame
        options_frame = ttk.LabelFrame(main_frame, text="Testing Type", padding="10")
        options_frame.pack(fill=tk.X, pady=10)
        
        # Development Testing Button
        dev_btn = ttk.Button(options_frame, text="🚧 Development Stage Test", 
                           command=self.run_development_test)
        dev_btn.pack(fill=tk.X, pady=5)
        
        # Production Testing Button
        prod_btn = ttk.Button(options_frame, text="🏭 Production Stage Test", 
                            command=self.run_production_test)
        prod_btn.pack(fill=tk.X, pady=5)
        
        # Results Area
        results_frame = ttk.LabelFrame(main_frame, text="Test Results", padding="10")
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.results_text = tk.Text(results_frame, height=15, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, 
                                command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def run_development_test(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return
        
        thread = threading.Thread(target=self._development_test_thread, args=(url,))
        thread.daemon = True
        thread.start()
    
    def run_production_test(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return
        
        thread = threading.Thread(target=self._production_test_thread, args=(url,))
        thread.daemon = True
        thread.start()
    
    def _development_test_thread(self, url):
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "🚧 Running DEVELOPMENT Tests...\n")
        self.results_text.insert(tk.END, "="*50 + "\n")
        
        try:
            tester = DevelopmentTester(url)
            results = tester.run_all_tests()
            self.display_results(results)
        except Exception as e:
            self.results_text.insert(tk.END, f"❌ Error: {str(e)}\n")
    
    def _production_test_thread(self, url):
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "🏭 Running PRODUCTION Tests...\n")
        self.results_text.insert(tk.END, "="*50 + "\n")
        
        try:
            tester = ProductionTester(url)
            results = tester.run_all_tests()
            self.display_results(results)
        except Exception as e:
            self.results_text.insert(tk.END, f"❌ Error: {str(e)}\n")
    
    def display_results(self, results):
        for test_name, result in results.items():
            status = "✅ PASS" if result['status'] else "❌ FAIL"
            self.results_text.insert(tk.END, f"\n{status} {test_name}\n")
            if result['details']:
                self.results_text.insert(tk.END, f"   Details: {result['details']}\n")
    
    def run(self):
        self.root.mainloop()