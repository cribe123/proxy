import proxyscrape
collector = proxyscrape.create_collector('my-collector', 'http')
proxy = collector.get_proxies({'country': 'france'})
print(f"{proxy.host}:{proxy.port} Анонимность: {proxy.anonymous} ({proxy.country.upper()})")