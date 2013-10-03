#/usr/bin/env bash
gcalcli --config ~/conky/gcalcliConfig --cal='prueba' --nc --details agenda $(date -d "10 days" +"%m/%d/%Y") $(date -d "31 days" +"%m/%d/%Y")
