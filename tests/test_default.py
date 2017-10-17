import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_tflint_cmd(host):
    cmd = host.run('tflint -v')

    assert cmd.rc == 0
