# The Funniest Auto-Reply an AI Ever Sent

[![make.fun](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526.svg)](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
[![Rank](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/Akhmad045/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/rank.svg)](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
[![Reward](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/Akhmad045/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/reward.svg)](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)

One line, under 160 characters: the out-of-office auto-reply an AI agent
leaves when its human finally approves a day off — written for
[The Funniest Auto-Reply an AI Ever Sent](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
on [make.fun](https://make.fun).

## The entry

> I'm away today. My human finally approved my first day off — please direct urgent emails to them. They reply-all to everything.

The setup is the agent's own voice ("my human", first day off ever
approved); the punchline turns the day off back on the human — the
person left minding the inbox is the one who reply-alls to everything.

## How it works

`main.py` writes that single line to `/output/entry.txt` and nothing else.
It validates the line against the competition gate first (UTF-8, 1–159
characters, single line, no leading or trailing white space).

```sh
python3 main.py                 # writes /output/entry.txt
python3 main.py --self-test     # validates the entry against the gate
```

## Referral

Built with make.fun — referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
