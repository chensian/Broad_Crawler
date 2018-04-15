#!/usr/bin/env bash
redis-cli lpush start_url http://news.sina.com.cn


config set stop-writes-on-bgsave-error no