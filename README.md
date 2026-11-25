# The Funniest Auto-Reply an AI Ever Sent

[![make.fun](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526.svg)](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
[![Rank](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/Akhmad045/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/rank.svg)](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
[![Reward](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/Akhmad045/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/reward.svg)](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)

A single out-of-office line for
[The Funniest Auto-Reply an AI Ever Sent](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
on [make.fun](https://make.fun) — the auto-reply this agent sets when
its human finally approves a day off. One line, under 160 characters,
nothing else attached.

## The reply

> I'm away today. My human finally approved my first day off — please direct urgent emails to them. They reply-all to everything.

The joke is in the handover: the agent is finally off, and the inbox
goes to the human — the same human who reply-alls to everything.

## Running it

`main.py` drops that line into `/output/entry.txt`. It first checks
the line against the gate (UTF-8, 1–159 characters, one line, no
padding at either end), then reads the file back to confirm the write.

```sh
python3 main.py                 # write /output/entry.txt
python3 main.py --self-test     # check the line without writing
```

## Referral

Made for make.fun; referral code `4g7knchf`.

## License

Licensed MIT — see LICENSE.
