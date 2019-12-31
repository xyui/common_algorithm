# -*- coding: utf-8 -*-

"""
利用快慢指针来判断链表中是否有环（并找出环的入口）
https://zhuanlan.zhihu.com/p/38521018

场景一：
经过起点、奇数
1 -> 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 9 -> 3
          ^
fast: 1->3->6->8->3->6->8->3->6->8->3->6->8->3->6->8->3->6->8
slow: 1->2->3->5->6->7->8->9->3->5->6->7->8->9->3->5->6->7->8->9
                        ^

找出环的入口
1 -> 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 9 -> 3
out                           in

####################################################################

场景二：
经过起点、偶数
1 -> 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 3
          ^
fast: 1->3->6->8->5->7->3->6->8->5->7->3->6->8->5->7
slow: 1->2->3->5->6->7->8->3->5->6->7->8->3->5->6->7->8->3->5->6->7->8
                     ^

找出环的入口
1 -> 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 3
out                      in

####################################################################

场景三：
不经过起点、奇数
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 4
               ^
fast: 1->3->5->7->9->5->7->9->5->7->9->5->7->9
slow: 1->2->3->4->5->6->7->8->9->4->5->6->7->8->9->4->5->6->7->8->9
                        ^

找出环的入口
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 4
out                           in

####################################################################

场景四：
不经过起点、偶数
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 4
               ^
fast: 1->3->5->7->4->6->8->5->7->4->6->8->5->7->4->6->8->5->7->4->6->8
slow: 1->2->3->4->5->6->7->8->4->5->6->7->8->4->5->6->7->8->4->5->6->7->8
                     ^
找出环的入口
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 4
out                      in

####################################################################

场景五：
1 -> 2 -> 1
^
fast: 1->1->1->1->1->1->1
slow: 1->2->1->2->1->2
            ^
找出环的入口
1 -> 2 -> 1
out
in

"""