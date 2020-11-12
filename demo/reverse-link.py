#!/usr/bin/env python
# -*- coding:utf-8 -*-
# owner:CSi
# datetime:2020/11/12 17:01
# software: PyCharm


class LinkNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):

    def reverse(self, node: LinkNode) -> None:
        cur, prev = node, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


if __name__ == '__main__':
    l1 = LinkNode(1)
    l2 = LinkNode(2)
    l3 = LinkNode(3)
    l4 = LinkNode(4)
    l5 = LinkNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    obj = Solution()
    print(obj.reverse(l1))
