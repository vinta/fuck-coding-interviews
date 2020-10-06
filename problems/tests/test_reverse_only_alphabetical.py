# coding: utf-8
from problems.reverse_only_alphabetical import reverse_only_alpha


def test_reverse_only_alpha():
    assert reverse_only_alpha('sea!$hells3') == 'sll!$ehaes3'
    assert reverse_only_alpha('1kas90jda3') == '1adj90sak3'


if __name__ == '__main__':
    test_reverse_only_alpha()
