#!/usr/bin/env python3
"""Dump ontology coverage as JSON."""

from skilldispatch.cli.commands import cmd_dump_ontology


class _Args:
    pass


if __name__ == "__main__":
    raise SystemExit(cmd_dump_ontology(_Args()))
