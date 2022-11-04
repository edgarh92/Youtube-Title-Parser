# -*- coding: utf-8 -*-
import unittest
from six import with_metaclass
from .meta import MetaTestSequence

tests = [
    {
        "input": "Rush – Moving Pictures (Full Album)",
        "expected": ["Rush", "Moving Pictures"],
    },
    {
        "input": "Rush – Moving Pictures (Audio)",
        "expected": ["Rush", "Moving Pictures"],
    },
    {
        "input": "runo plum - black pepper #alternative #indie",
        "expected": ["runo plum", "black pepper"],
    },
    {
        "input": "Rush - Moving Pictures (album)",
        "expected": ["Rush", "Moving Pictures"],
    },
    {
        "input": "[MV] 김뜻돌 (Meaningful Stone) - 비 오는 거리에서 춤을 추자 (Dancing in the rain) / Official Music Video",
        "expected": ["김뜻돌", "비 오는 거리에서 춤을 추자"],
    },
    {
        "input": "Rush - Moving Pictures (Full Album) (Official)",
        "expected": ["Rush", "Moving Pictures"],
    },
    {
        "input": "FILMMAKER - ETERNAL RETURN [FULL ALBUM]",
        "expected": ["FILMMAKER", "ETERNAL RETURN"],
    },
    {
        "input": "Dua Lipa - New Rules (Official Music Video) **NEW**",
        "expected": ["Dua Lipa", "New Rules"],
    },
    {
        "input": "Muse — The 2nd Law (Full Album) [HD]",
        "expected": ["Muse", "The 2nd Law"],
    },
    {
        "input": ["[또 오해영 OST Part 5] 정승환 (Jung Seung-Hwan) - 너였다면 (If It Is You)"],
        "expected": ["정승환", "너였다면"],
    },
    {
        "input": "SAYAKA「garden」",
        "expected": ["SAYAKA", "garden"],
    }

]


class TestSequence(with_metaclass(MetaTestSequence, unittest.TestCase)):
    test_cases = tests
    test_type = __file__


if __name__ == "__main__":
    unittest.main()
