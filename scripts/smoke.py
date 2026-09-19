import json,secrets,time
from pathlib import Path
from genlayer_py import create_client,create_account
from genlayer_py.chains import studionet
R=Path(__file__).parents[1];E=(R.parents[3]/'accounts.env').read_text();v=lambda n:next(x.split('=',1)[1].strip().strip('"').strip("'") for x in E.splitlines() if x.startswith(n+'='));owner=create_account(account_private_key=v('ACCOUNT_6_GENLAYER_PRIVATE_KEY'));member=create_account(account_private_key='0x'+secrets.token_hex(32));co=create_client(chain=studionet,account=owner);cm=create_client(chain=studionet,account=member);addr='0x44E3d841eBf003C94280B45769E5016b13a8d851';rid='LIVE-'+str(int(time.time()));commit='dc2827f';weather=f'https://raw.githubusercontent.com/wakbowaa/water-turn/{commit}/evidence/weather.txt';flow=f'https://cdn.jsdelivr.net/gh/wakbowaa/water-turn@{commit}/evidence/flow.txt';tx=[]
def send(client,fn,args):
 h=client.write_contract(address=addr,function_name=fn,args=args);r=client.wait_for_transaction_receipt(transaction_hash=h,status='FINALIZED',retries=180,interval=5000);assert r.get('status_name')=='FINALIZED';tx.append(h)
send(co,'schedule',[rid,member.address,'North orchard channel',100000,90,weather,flow]);send(cm,'request_exception',[rid,121600,weather,flow]);send(cm,'close',[rid]);print(json.dumps({'id':rid,'state':'CLOSED','transactions':tx}),flush=True)
