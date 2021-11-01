# file: files/shells/init.sls

disable_dash:
  file.comment:
    - name: /etc/shells
    - regex: ^\/bin\/dash
