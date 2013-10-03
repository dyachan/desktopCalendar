#/usr/bin/env bash
gcalcli --config ~/conky/gcalcliConfig --nc --details agenda $(date +"%m/%d/%Y") $(date -d "21 days" +"%m/%d/%Y")
