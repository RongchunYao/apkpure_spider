#-*- coding: utf-8 -*-
#modify config file if u want.
#u may use different proxies and cookies in turn just add here and modify api in py files to lower down the chance that ip got banned

my_proxy = {'http':'socks5://127.0.0.1:1080','https':'socks5h://127.0.0.1:1080'}
key_wd = ['chatbot']
my_headers={
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"cache-control": "max-age=0",
"upgrade-insecure-requests": "1"
}
#make sure to change cookie to your cookie or just comment it
my_headers["cookie"]="__cfduid=dc4f6977be31cb83f064419310ded65661540542077; _ga=GA1.2.1950587501.1540542078; _gid=GA1.2.1198378188.1540894083; apkpure__lang=en; AMP_TOKEN=%24NOT_FOUND; __atuvc=26%7C43%2C37%7C44; __atuvs=5bd94f5b603b2944002"
my_headers["user-agent"]="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"

