ansible_role_tflint
=========

Set up [tflint][https://github.com/wata727/tflint] utility.


Requirements
------------

The role has been tested on the following stack:

  * CentOS 7

Dependencies
------------

  * [ansible_role_unzip](https://github.com/mauromedda/ansible_role_unzip)

Role Variables
--------------

| parameter           | required | default                                             |  
| ---------           | -------- | -------                                             |
| tflint_bin_dir      | yes      | /usr/local/tflint/bin                               |
| tflint_v            | yes      | v0.5.0                                              |    
| tflint_zip_file     | yes      | tflint_linux_amd64.zip                              |     
| tflint_release_repo | yes      | https://github.com/wata727/tflint/releases/download |


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ansible_role_tflint, tflint_v: v0.5.1 }

License
-------

BSD

Author Information
------------------

misurellig < bejohnzorn at gmail dot com >
