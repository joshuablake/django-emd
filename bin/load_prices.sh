#!/usr/bin/env bash
USER=root
DATABASE=wspacekills
cd /tmp
wget http://eve-marketdata.com/developers/mysql_items_history_10000001.txt.gz
gunzip mysql_items_history_10000001.txt.gz
mysql -u$USER -D$DATABASE < create_prices.sql
mysql -u$USER -D$DATABASE < mysql_items_history_10000001.txt
mysql -u$USER -D$DATABASE -e "ALTER TABLE items_history ADD COLUMN `id` int PRIMARY KEY AUTO_INCREMENT"
