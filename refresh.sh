sudo cp minecraft-web-page.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable minecraft-web-page.service
systemctl restart minecraft-web-page.service