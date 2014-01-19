#/usr/bin/env bash
gcalcli --config ~/conky/gcalcliConfig --nc --cals default --details agenda $(date +"%m/%d/%Y") $(date -d "23 days" +"%m/%d/%Y")
