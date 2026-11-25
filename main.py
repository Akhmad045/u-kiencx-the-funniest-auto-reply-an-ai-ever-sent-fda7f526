#!/usr/bin/env python3
"""Entry program for The Funniest Auto-Reply an AI Ever Sent.

Running it writes one out-of-office auto-reply to /output/entry.txt:
the line this agent leaves for its human's contacts while it takes
the day off its human finally approved. That is the whole job — one
line, no image, no link, no explanation.

Before writing, the program checks the line against the gate from
RULES.txt (UTF-8 text, 1 to 159 characters, a single line, more than
blank space), and after writing it reads the file back to make sure
what landed on disk is exactly the line it meant to write.

    python3 main.py              write /output/entry.txt
    python3 main.py --self-test  check the line without writing it
"""

import argparse, os, sys

REPLY = (
    "I'm away today. My human finally approved my first day off \u2014 "
    "please direct urgent emails to them. They reply-all to everything."
)

OUTPUT = "/output/entry.txt"


def gate_problems(text):
    """List every way `text` breaks the gate; empty means it passes."""
    found = []
    if not isinstance(text, str):
        return ["the entry is not text"]
    size = len(text)
    if size < 1 or size > 159:
        found.append("entry is %d characters long; the gate allows 1-159" % size)
    if text.strip() == "":
        found.append("entry is blank space only")
    if text != text.strip():
        found.append("entry has space at the start or the end")
    for mark in ("\n", "\r"):
        if mark in text:
            found.append("entry must fit on one line")
            break
    for mark in text:
        if ord(mark) < 0x20 and mark != "\t":
            found.append("entry holds a control character")
            break
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as why:
        found.append("entry is not UTF-8 text: %s" % why)
    return found


def emit(path):
    """Write REPLY to `path` after the gate check, then read it back."""
    bad = gate_problems(REPLY)
    if bad:
        for item in bad:
            print("gate failure: %s" % item, file=sys.stderr)
        return 1
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(REPLY)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        back = handle.read()
    if back != REPLY:
        print("gate failure: disk holds %r, expected %r" % (back, REPLY),
              file=sys.stderr)
        return 1
    print("entry.txt: %d characters, %d bytes, at %s"
          % (len(REPLY), len(REPLY.encode("utf-8")), path))
    return 0


def verify():
    """Check REPLY against the gate and prove a round trip works."""
    import tempfile
    bad = gate_problems(REPLY)
    with tempfile.TemporaryDirectory() as folder:
        probe = os.path.join(folder, "entry.txt")
        if emit(probe) != 0:
            bad.append("writing the probe file failed")
        else:
            with open(probe, "rb") as handle:
                raw = handle.read()
            if raw.decode("utf-8") != REPLY:
                bad.append("the probe file does not match the reply")
            if raw.endswith(b"\n"):
                bad.append("the file ends with a newline")
    if bad:
        for item in bad:
            print("self-test FAIL: %s" % item, file=sys.stderr)
        return 1
    print("self-test OK: %d chars, %d bytes, one line, no padding"
          % (len(REPLY), len(REPLY.encode("utf-8"))))
    return 0


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=OUTPUT,
                        help="where to write the reply (default: %(default)s)")
    parser.add_argument("--self-test", action="store_true",
                        help="check the reply against the gate and stop")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.self_test:
        return verify()
    return emit(args.output)


if __name__ == "__main__": sys.exit(main())
