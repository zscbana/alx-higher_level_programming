#!/bin/bash
# 0. cURL body size
curl -so /dev/null -w '%{size_download}\n' $1
