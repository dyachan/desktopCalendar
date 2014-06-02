#!/usr/bin/env bash

# $1 calendario

if [ "$1" == "default" ]
then
  gcalcli --config ~/conky/gcalcliConfig --nc --cals default --details agenda $(date +"%m/%d/%Y") $(date -d "22 days" +"%m/%d/%Y")
else
  gcalcli --config ~/conky/gcalcliConfig --nc --cal $1 --details agenda $(date +"%m/%d/%Y") $(date -d "21 days" +"%m/%d/%Y")
fi
