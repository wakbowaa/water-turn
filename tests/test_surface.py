from pathlib import Path
T=Path('contracts/contract.py').read_text(encoding='utf-8');P=Path('docs/index.html').read_text(encoding='utf-8')
def test_surface():
 for n in ('schedule','request_exception','close','get_turn'):assert 'def '+n in T and n in P
 assert "status:'FINALIZED'" in P and 'id="river"' in P and 'id="sluice"' in P
