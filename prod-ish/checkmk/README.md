# Checkmk doc

1 to 13

2 Beginners guide

Setting up Checkmk

The CRE Checkmk Raw Edition is free, 100 % Open Source and incorporates Nagios as its core. You can use it to comprehensively monitor complex environments. Support is available in our Forum from the Checkmk community.

https://docs.checkmk.com/latest/en/cse.html?lquery=raw

https://docs.checkmk.com/latest/en/


## Visuals

https://follow-e-lo.com/2024/02/16/checkmk-one-line/


## Topology and Monitoring agents

* Port 6556
* The agents are passive in pull mode and listen on TCP port 6556. Only on receiving a Checkmk server query will these agents be activated and respond with the required data.
* In push mode, on the other hand, the Checkmk agent periodically sends the monitoring data to the Checkmk server on its own.
* * The push mode is always required if the Checkmk server cannot access the network in which the host to be monitored and its agent are located, for example, in a cloud-based configuration. For this reason, the push mode only exists in the CSE Checkmk Cloud Edition.

https://docs.checkmk.com/latest/en/wato_monitoringagents.html


## Custom agent

https://docs.checkmk.com/latest/en/devel_check_plugins.html

https://www.reddit.com/r/nagios/comments/aq1zg5/how_to_create_a_customized_check_in_check_mk/

## Writing agent-based check plug-ins



https://docs.checkmk.com/latest/en/devel_check_plugins.html?lquery=custom%20check

## Backend

There is no database involved in a check_mk monitoring site.

All data is stored in files in the sites directory, usually under ~/var.
You will find there logfiles containing the events and RRD files
containing the performance data.

https://forum.checkmk.com/t/check-mk-english-check-mk-storing-data-question/11922/3

## Basic information on the installation of Checkmk

https://docs.checkmk.com/latest/en/install_packages.html

## Installation as a Docker container

https://docs.checkmk.com/latest/en/introduction_docker.html


## Monitoring agents

https://docs.checkmk.com/latest/en/wato_monitoringagents.html


## Rules In Checkmk you configure parameters for hosts and services by using rules.

https://docs.checkmk.com/latest/en/wato_rules.html

## How To Monitor Server Health with Checkmk 2.0 on Ubuntu 20.04

https://mail.google.com/mail/u/0/#inbox/QgrcJHshZXmGgnkrwKnBkmNqRfmDBKPjQQB


## Checkmk Ubuntu

## Checkmk Docker

https://docs.checkmk.com/latest/en/introduction_docker.html?lquery=docker

