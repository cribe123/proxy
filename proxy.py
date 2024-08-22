import proxyscrape
collector = proxyscrape.create_collector('my-collector', 'http')
proxy = collector.get_proxies({'country': 'france'})
print(proxy)