#!/bin/bash
if [ ! -f "/usr/bin/clear-cache.py" ];then
curl -o /usr/bin/clear-cache.py -L https://raw.githubusercontent.com/Ccapton/myshell/master/clear-cache/clear-cache.py
chmod +x /usr/bin/clear-cache.py
fi
nohup python3 /usr/bin/clear-cache.py >/dev/null 2>log &

