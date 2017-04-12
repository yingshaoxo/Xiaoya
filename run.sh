pkill python
ssserver -c /root/ss.json -d start
nohup python3 @API_server.py &
nohup python3 Telegram.py &
