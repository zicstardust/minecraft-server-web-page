git pull
cp minecraft-web-page.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable minecraft-web-page.service
sudo systemctl restart minecraft-web-page.service