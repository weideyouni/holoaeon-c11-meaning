# -*- coding: utf-8 -*-
"""C11 Gate —— 意义仓（意义枢纽·主相枢纽/副相木）
================================================================================
  · 第一性原理问题：这件事对我意味着什么
  · 神龟（保存基线族）：保存价值基线与意义锚点
  · 神马（推演路径族）：推演意义重构与方向调整
  · N19 派生声明：本仓=N19 holoaeon（github.com/weideyouni/holoaeon，唯一归零
    锚·唯一全局观测者）机制在本领域的正交投影。机制不在本仓重写——
    复用映射见 README（指针纪律的仓库版：派生装配，不复制实现）。
  · 集群账本：holoaeon/c18_cluster.py（19×19 耦合矩阵+边 Schema）。
  · 纯标准库零依赖·独立可运行（clone 即跑）。
"""
from __future__ import annotations

import hashlib
import json
import sys
from typing import List

CANG_ID = "C11"
REPO = "holoaeon-c11-meaning"
DOMAIN = "意义"
QUESTION = "这件事对我意味着什么"
PHASE_MAIN = "枢纽"
PHASE_SUB = "木"
ROLE = "意义枢纽"
TURTLE = "保存价值基线与意义锚点"
HORSE = "推演意义重构与方向调整"
SEAL = "潮起开门，潮落闭嘴"

CHAIN = {
    "id": CANG_ID,
    "repo": REPO,
    "n19_anchor": "github.com/weideyouni/holoaeon",
    "cluster_ledger": "holoaeon/c18_cluster.py",
    "ring": 19,
    "batch": "V55",
}


class CangGate:
    """C11 总闸：注册完整性自检（同构骨架·S1/S2 可测）。"""

    def self_check(self) -> dict:
        fields_ok = all([CANG_ID, REPO, DOMAIN, QUESTION, PHASE_MAIN,
                         PHASE_SUB, ROLE, TURTLE, HORSE])
        return {
            "ok": fields_ok and CANG_ID.startswith("C") and
                  REPO.startswith("holoaeon-c"),
            "cang_id": CANG_ID, "domain": DOMAIN, "phase_main": PHASE_MAIN,
            "seal": SEAL,
        }


def probe() -> dict:
    return CangGate().self_check()


def fingerprint() -> dict:
    return {
        "cang": CANG_ID, "repo": REPO, "domain": DOMAIN,
        "sha256": hashlib.sha256(
            ("%s-v1:" % REPO + SEAL).encode("utf-8")).hexdigest(),
        "seal": SEAL,
    }


def _main(argv: List[str]) -> int:
    cmd = argv[1] if len(argv) > 1 else "probe"
    if cmd == "probe":
        out = probe()
    elif cmd == "fingerprint":
        out = fingerprint()
    else:
        print("usage: python -m holoaeon_c11_meaning [probe|fingerprint]",
              file=sys.stderr)
        return 2
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out.get("ok", True) else 1


if __name__ == "__main__":
    raise SystemExit(_main(["c11_meaning"] + sys.argv[1:]))
