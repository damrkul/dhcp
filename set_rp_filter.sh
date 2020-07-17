#!/bin/bash
echo Setting rp_filter to 0 for enp0s8 and all
echo 0 > /proc/sys/net/ipv4/conf/enp0s8/rp_filter
echo 0 > /proc/sys/net/ipv4/conf/all/rp_filter
