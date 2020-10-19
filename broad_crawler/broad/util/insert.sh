#!/usr/bin/env bash

redis-cli lpush start_url https://finance.sina.com.cn


redis-cli lpush start_url http://guba.eastmoney.com/

config set stop-writes-on-bgsave-error no