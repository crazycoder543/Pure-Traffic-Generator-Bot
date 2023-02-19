from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

# Read the URLs from the file
with open('links.txt', 'r') as f:
    urls = [line.strip() for line in f]

# Read proxy IP addresses and port numbers from file
with open('proxy.txt', 'r') as f:
    proxies = [line.strip() for line in f]

# Loop through each proxy and URL
for proxy in proxies:
    for url in urls:
        # Define the proxy server
        prox = Proxy()
        prox.proxy_type = ProxyType.MANUAL
        prox.http_proxy = proxy
        prox.ssl_proxy = proxy

        # Define the options for the webdriver with the proxy server
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server={}:{}'.format(prox.http_proxy.split(':')[0], prox.http_proxy.split(':')[1]))

        # Create a new webdriver with the options
        driver = webdriver.Chrome(options=options)

        # Navigate to the URL
        driver.get(url)

        # Wait for the page to load
        time.sleep(5)
        
        # Close the browser
        driver.close()
