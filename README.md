# Water Turn

> Move the hour. Never steal the minutes.

Irrigation cooperatives regularly need to shift a member's slot because of heat or canal conditions. A casual reschedule can hide a quieter failure: the member receives less water. Water Turn makes the distinction explicit.

## The rule of the channel

```
scheduled duration ───────────────────────────────┐
weather authority ──┐                            │
flow authority ─────┴─ consensus decision ───────┼─> adjusted / denied
member request ───────────────────────────────────┘
```

`schedule` freezes the member, channel, duration, and two independent authority origins. Only that member can call `request_exception`. Validators fetch both records, hash the bytes, and independently judge whether the move is justified. The stored allocation never changes. `close` then seals the decided turn.

## Reproduce it

```powershell
pytest -q
ruff check contracts tests
python scripts/deploy.py
```

The browser surface is an animated channel schedule, not a substitute for the contract. It names every callable and, after deployment, pins the StudioNet address and live evidence in `deployment.json`.

## Review trail

- Contract: `contracts/contract.py`
- Direct tests: `tests/direct/test_turn.py`
- Two independent field records: `evidence/`
- Deployment and transaction receipts: `deployment.json`

Security boundaries include fixed HTTPS origins, a ±24-hour movement bound, member-only requests, a 15–720 minute allocation range, deterministic validator comparison, and persisted SHA-256 digests.
