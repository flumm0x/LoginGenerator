#!/bin/bash
#e-mail disk util every hour

df -h | mail -s "disk space" KRKahn@gmail.com
