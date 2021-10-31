# file: files/top.sls
#
# Salt states top file
#

base:

    '*':
        - ntp
