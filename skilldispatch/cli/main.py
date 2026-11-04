"""CLI entrypoint: python -m skilldispatch.cli ..."""

from __future__ import annotations

import argparse

from skilldispatch.cli.commands import cmd_demo, cmd_dump_ontology, cmd_pivot


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="skilldispatch", description="Skilldispatch CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    demo = sub.add_parser("demo", help="Run the canned pivot demo")
    demo.set_defaults(func=cmd_demo)

    pivot = sub.add_parser("pivot", help="Run a one-off pivot")
    pivot.add_argument("--skills", required=True)
    pivot.add_argument("--years", type=int, default=3)
    pivot.set_defaults(func=cmd_pivot)

    dump = sub.add_parser("dump-ontology", help="Print ontology coverage stats")
    dump.set_defaults(func=cmd_dump_ontology)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args) or 0)


if __name__ == "__main__":
    raise SystemExit(main())
