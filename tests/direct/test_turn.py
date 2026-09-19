from conftest import CONTRACT
def test_adjusted_without_allocation_change(direct_vm,direct_deploy,direct_alice,direct_bob):
 direct_vm.sender=direct_alice;x=direct_deploy(CONTRACT);x.schedule('t-1','0x'+direct_bob.hex(),'North channel',100000,90,'https://weather.example/base','https://flow.example/base');direct_vm.sender=direct_bob;direct_vm.mock_web(r'weather\.example',{'status':200,'body':'Severe heat at baseline slot.'});direct_vm.mock_web(r'flow\.example',{'status':200,'body':'Adequate flow six hours later.'});direct_vm.mock_llm(r'.*WaterTurn exception check.*','{"justified":true,"reason":"Heat and flow justify shift."}');x.request_exception('t-1',121600,'https://weather.example/report','https://flow.example/report');r=x.get_turn('t-1');assert r['state']=='ADJUSTED' and r['minutes']==90
def test_member_only(direct_vm,direct_deploy,direct_alice,direct_bob):
 direct_vm.sender=direct_alice;x=direct_deploy(CONTRACT);x.schedule('t-1','0x'+direct_bob.hex(),'North channel',100000,90,'https://weather.example/base','https://flow.example/base')
 with direct_vm.expect_revert('bounded member'):x.request_exception('t-1',121600,'https://weather.example/report','https://flow.example/report')
