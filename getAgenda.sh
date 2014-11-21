#!/usr/bin/env bash

gcalcli --config config_gcalcli --nocolor --detail_calendar agenda $(date +"%m/%d/%Y") $(date -d "22 days" +"%m/%d/%Y")

# $1 calendario

#if [ "$1" == "default" ]
#then
#  gcalcli --config ~/conky/config_gcalcli --nocolor --cals default --detail-all agenda $(date +"%m/%d/%Y") $(date -d "22 days" +"%m/%d/%Y")
#else
#  gcalcli --config ~/conky/config_gcalcli --nocolor --cal $1 --detail-all agenda $(date +"%m/%d/%Y") $(date -d "21 days" +"%m/%d/%Y")
#fi
