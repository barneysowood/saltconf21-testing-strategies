# file: files/ntp/init.sls

{%- set pkg_name = "ntp" %}

install_ntp:
  pkg.installed:
    - name: {{ pkg_name }}

configure_ntp:
  file.managed:
    - name: /etc/ntp.conf
    - source: salt://ntp/files/ntp.conf
    - template: jinja
    - user: root
    - group: root
    - mode: '0640'

restart_ntp_on_changes:
  service.running:
    - name: ntp
    - enable: True
    - watch_any:
      - pkg: install_ntp
      - file: configure_ntp
