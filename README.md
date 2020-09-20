# fuck-coding-interviews

[![build](https://img.shields.io/github/workflow/status/vinta/fuck-coding-interviews/CI?style=flat-square)](https://github.com/vinta/fuck-coding-interviews/actions)
[![coverage](https://img.shields.io/codecov/c/github/vinta/fuck-coding-interviews?style=flat-square)](https://codecov.io/gh/vinta/fuck-coding-interviews)
[![requirements](https://img.shields.io/requires/github/vinta/fuck-coding-interviews?style=flat-square)](https://requires.io/github/vinta/fuck-coding-interviews/requirements/)

This repository is created by [a clumsy programmer](https://leetcode.com/vinta/) who always struggles with coding problems on LeetCode, even with some **Easy** questions.

> How on earth can I ever think of a solution like that in an interview?!

I'm working on implementing common Algorithms and Data Structures in Python (with test cases, of course), as well as straightforward solutions to some problems from LeetCode, HackerRank, and HackerEarth which I solved with frustration in mind.

Well, there are SO MUCH things to learn in Computer Science. I'm just a peasant who happens to write some crappy code for living.

**This project requires Python 3.6 or higher.**

## No Whiteboards

[Hiring Without Whiteboards](https://github.com/poteto/hiring-without-whiteboards)

A list of companies (or teams) that don't do "whiteboard" interviews.

> - Discussing a real world problem (with or without whiteboard) is 👍
> - Solving CS trivia, technical puzzles, riddles, brainteasers (with or without whiteboard) is 👎

## Contents

- `algorithms/`
    - `hashing/`
        - [MAD (Multiply-Add-Divide) compression function](https://github.com/vinta/fuck-coding-interviews/blob/master/algorithms/hashing/mad_compression.py)
    - `math/`
        - [Factorial number](https://github.com/vinta/fuck-coding-interviews/blob/master/algorithms/math/factorial.py)
        - [Fibonacci number](https://github.com/vinta/fuck-coding-interviews/blob/master/algorithms/math/fibonacci.py)
    - `searching/`
        - [Linear Search](https://github.com/vinta/fuck-coding-interviews/blob/master/algorithms/searching/linear_search.py)
        - [Binary Search](https://github.com/vinta/fuck-coding-interviews/blob/master/algorithms/searching/binary_search.py)
        - [Binary Search the first appeared position](https://github.com/vinta/fuck-coding-interviews/blob/master/algorithms/searching/binary_search_left_bound.py)
    - `sorting/`
        - [Bubble Sort](https://github.com/vinta/fuck-coding-interviews/blob/master/algorithms/sorting/bubble_sort.py)
        - [Heap Sort](https://github.com/vinta/fuck-coding-interviews/blob/master/algorithms/sorting/heap_sort.py)
        - [Insertion Sort](https://github.com/vinta/fuck-coding-interviews/blob/master/algorithms/sorting/insertion_sort.py)
        - [Quick Sort](https://github.com/vinta/fuck-coding-interviews/blob/master/algorithms/sorting/quick_sort.py)
        - [Selection Sort](https://github.com/vinta/fuck-coding-interviews/blob/master/algorithms/sorting/selection_sort.py)
- `data_structures/`
    - `arrays/`
        - [Circular Array](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/arrays/circular_array.py)
        - [Dynamic Array](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/arrays/dynamic_array.py)
    - `b_trees/`
        - [B-tree](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/b_trees/b_tree.py)
        - [B+ Tree](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/b_trees/b_plus_tree.py)
    - `graphs/`
        - [Directed Weighted Graph implemented with Adjacency Map](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/graphs/adjacency_map_directed_weighted_graph.py)
        - [Undirected Weighted Graph implemented with Adjacency Map](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/graphs/adjacency_map_undirected_weighted_graph.py)
    - `hash_maps/`
        - [Sorted TableMap](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/hash_maps/sorted_table_map.py)
        - [Unsorted TableMap](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/hash_maps/unsorted_table_map.py)
        - [HashMap implemented with Separate Chaining](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/hash_maps/chain_hash_map.py)
        - [HashMap implemented with Linear Probing](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/hash_maps/linear_probing_hash_map.py)
    - `heaps/`
        - [Binary Heap implemented with Array](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/heaps/array_based_binary_heap.py)
    - `linked_lists/`
        - [Singly Linked List](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/linked_lists/singly_linked_list.py)
        - [Doubly Linked List](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/linked_lists/doubly_linked_list.py)
    - `queues/`
        - [Queue implemented with Array](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/queues/array_based_queue.py)
        - [Queue implemented with Circular Array](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/queues/circular_array_based_queue.py)
        - [Queue implemented with Linked List](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/queues/linked_list_based_queue.py)
        - [Double-ended Queue implemented with Doubly Linked List](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/queues/doubly_linked_list_based_deque.py)
        - [Priority Queue implemented with Heap](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/queues/heap_based_priority_queue.py)
    - `sets/`
        - [Set implemented with HashMap](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/sets/hash_map_based_set.py)
        - [Multiset implemented with HashMap](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/sets/hash_map_based_multiset.py)
    - `stacks/`
        - [Stack implemented with Array](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/stacks/array_based_stack.py)
        - [Stack implemented with Linked List](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/stacks/linked_list_based_stack.py)
    - `trees/`
        - [Binary Search Tree](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/trees/binary_search_tree.py)
        - [Binary Tree Serialization](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/trees/binary_tree_serialization.py)
        - [Treap](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/trees/treap.py)
        - [Trie](https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/trees/trie.py)
- `problems/`
    - Array
        - [Array Sum](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/array_sum.py) from [HackerEarth](https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/array-sum-2-725368ac/description/)
        - [Find Minimum in Rotated Sorted Array](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/find_minimum_in_rotated_sorted_array.py) from [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
        - [Maximum Product Subarray](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/maximum_product_subarray.py) from [LeetCode](https://leetcode.com/problems/maximum-product-subarray/)
        - [Maximum Subarray](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/maximum_subarray.py) from [LeetCode](https://leetcode.com/problems/maximum-subarray/)
        - [Merge Intervals](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/merge_intervals.py) from [LeetCode](https://leetcode.com/problems/merge-intervals/)
        - [Product of Array Except Self](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/product_of_array_except_self.py) from [LeetCode](https://leetcode.com/problems/product-of-array-except-self/)
        - [Search in Rotated Sorted Array](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/search_in_rotated_sorted_array.py) from [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)
        - [Subsets](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/subsets.py) from [LeetCode](https://leetcode.com/problems/subsets/)
    - Linked List
        - [Add Two Numbers](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/add_two_numbers.py) from [LeetCode](https://leetcode.com/problems/add-two-numbers/)
        - [Linked List Cycle](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/linked_list_cycle.py) from [LeetCode](https://leetcode.com/problems/linked-list-cycle/)
        - [Merge Two Sorted Lists](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/merge_two_sorted_lists.py) from [LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)
        - [Remove Nth Node From End of List](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/remove_nth_node_from_end_of_list.py) from [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
        - [Reverse Linked List](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/reverse_linked_list.py) from [LeetCode](https://leetcode.com/problems/reverse-linked-list/)
    - String
        - [CamelCase](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/camel_case.py) from [HackerRank](https://www.hackerrank.com/challenges/camelcase/problem)
        - [Group Anagrams](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/group_anagrams.py) from [LeetCode](https://leetcode.com/problems/group-anagrams/)
        - [Implement strStr()](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/implement_strstr.py) from [LeetCode](https://leetcode.com/problems/implement-strstr/)
        - [Is Subsequence](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/is_subsequence.py) from [LeetCode](https://leetcode.com/problems/is-subsequence/)
        - [Pangrams](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/pangrams.py) from [HackerRank](https://www.hackerrank.com/challenges/pangrams/problem)
        - [Repeated String](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/repeated_string.py) from [HackerRank](https://www.hackerrank.com/challenges/repeated-string/problem)
        - [Reverse Integer](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/reverse_integer.py) from [LeetCode](https://leetcode.com/problems/reverse-integer/)
        - [Valid Anagram](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/valid_anagram.py) from [LeetCode](https://leetcode.com/problems/valid-anagram/)
    - HashMap
        - [2 Sum](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/two_sum.py) from [LeetCode](https://leetcode.com/problems/two-sum/)
        - [3 Sum](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/three_sum.py) from [LeetCode](https://leetcode.com/problems/3sum/)
    - Set
        - [Contains Duplicate](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/contains_duplicate.py) from [LeetCode](https://leetcode.com/problems/contains-duplicate/)
    - Multiset
        - [Equalize the Array](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/equality_in_a_array.py) from [HackerRank](https://www.hackerrank.com/challenges/equality-in-a-array/problem)
        - [Top K Frequent Elements](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/top_k_frequent_elements.py) from [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)
    - Heap
        - [Kth Largest Element in an Array](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/kth_largest_element_in_an_array.py) from [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/)
        - [Merge k Sorted Lists](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/merge_k_sorted_lists.py) from [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)
        - [Task Scheduler](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/task_scheduler.py) from [LeetCode](https://leetcode.com/problems/task-scheduler/)
    - Stack
        - [Maximum Element](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/maximum_element.py) from [HackerRank](https://www.hackerrank.com/challenges/maximum-element/problem)
        - [Min Stack](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/min_stack.py) from [LeetCode](https://leetcode.com/problems/min-stack/)
        - [Valid Parentheses](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/valid_parentheses.py) from [LeetCode](https://leetcode.com/problems/valid-parentheses/)
    - Binary Tree
        - [Balanced Binary Tree](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/balanced_binary_tree.py) from [LeetCode](https://leetcode.com/problems/balanced-binary-tree/)
        - [Binary Search Tree Iterator](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/binary-search-tree-iterator.py) from [LeetCode](https://leetcode.com/problems/binary-search-tree-iterator/)
        - [Binary Tree Inorder Traversal](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/binary_tree_inorder_traversal.py) from [LeetCode](https://leetcode.com/problems/binary-tree-inorder-traversal/)
        - [Binary Tree Level Order Traversal](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/binary_tree_level_order_traversal.py) from [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)
        - [Binary Tree Postorder Traversal](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/binary_tree_postorder_traversal.py) from [LeetCode](https://leetcode.com/problems/binary-tree-postorder-traversal/)
        - [Binary Tree Preorder Traversal](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/binary_tree_preorder_traversal.py) from [LeetCode](https://leetcode.com/problems/binary-tree-preorder-traversal/)
        - [Check Completeness of a Binary Tree](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/check_completeness_of_a_binary_tree.py) from [LeetCode](https://leetcode.com/problems/check-completeness-of-a-binary-tree/)
        - [Find Mode in Binary Search Tree](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/find_mode_in_binary_search_tree.py) from [LeetCode](https://leetcode.com/problems/find-mode-in-binary-search-tree/)
        - [Invert Binary Tree](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/invert_binary_tree.py) from [LeetCode](https://leetcode.com/problems/invert-binary-tree/)
        - [Kth Smallest Element in a BST](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/kth_smallest_element_in_a_bst.py) from [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
        - [Maximum Depth of Binary Tree](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/maximum_depth_of_binary_tree.py) from [LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
        - [Minimum Depth of Binary Tree](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/minimum_depth_of_binary_tree.py) from [LeetCode](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
        - [Same Tree](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/same_tree.py) from [LeetCode](https://leetcode.com/problems/same-tree/)
        - [Search in a Binary Search Tree](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/search_in_a_binary_search_tree.py) from [LeetCode](https://leetcode.com/problems/search-in-a-binary-search-tree/)
        - [Serialize and Deserialize Binary Tree](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/serialize_and_deserialize_binary_tree.py) from [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
        - [Tree: Height of a Binary Tree](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/tree_height_of_a_binary_tree.py) from [HackerRank](https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem)
        - [Tree: Top View](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/tree_top_view.py) from [HackerRank](https://www.hackerrank.com/challenges/tree-top-view/problem)
        - [Univalued Binary Tree](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/univalued_binary_tree.py) from [LeetCode](https://leetcode.com/problems/univalued-binary-tree/)
        - [Validate Binary Search Tree](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/validate_binary_search_tree.py) from [LeetCode](https://leetcode.com/problems/validate-binary-search-tree/)
    - Trie
        - [Implement Trie (Prefix Tree)](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/implement_trie_prefix_tree.py) from [LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/)
    - Graph
        - [BFS: Shortest Reach in a Graph](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/ctci_bfs_shortest_reach.py) from [HackerRank](https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem)
        - [Clone Graph](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/clone_graph.py) from [LeetCode](https://leetcode.com/problems/clone-graph/)
    - SQL
        - [Big Countries](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/big_countries.sql) from [LeetCode](https://leetcode.com/problems/big-countries/)
        - [Nth Highest Salary](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/nth_highest_salary.sql) from [LeetCode](https://leetcode.com/problems/nth-highest-salary/)
        - [Rank Scores](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/rank_scores.sql) from [LeetCode](https://leetcode.com/problems/rank-scores/)
        - [Second Highest Salary](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/second_highest_salary.sql) from [LeetCode](https://leetcode.com/problems/second-highest-salary/)
    - Uncategorized
        - [Best Time to Buy and Sell Stock](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/best_time_to_buy_and_sell_stock.py) from [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
        - [Container With Most Water](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/container_with_most_water.py) from [LeetCode](https://leetcode.com/problems/container-with-most-water/)
        - [Counting Valleys](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/counting_valleys.py) from [HackerRank](https://www.hackerrank.com/challenges/counting-valleys/problem)
        - [Fibonacci Number](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/fibonacci_number.py) from [LeetCode](https://leetcode.com/problems/fibonacci-number/)
        - [Fizz Buzz](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/fizz_buzz.py) from [LeetCode](https://leetcode.com/problems/fizz-buzz/)
        - [Jumping on the Clouds](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/jumping_on_the_clouds.py) from [HackerRank](https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem)
        - [Mars Exploration](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/mars_exploration.py) from [HackerRank](https://www.hackerrank.com/challenges/mars-exploration/problem)
        - [Sock Merchant](https://github.com/vinta/fuck-coding-interviews/blob/master/problems/sock_merchant.py) from [HackerRank](https://www.hackerrank.com/challenges/sock-merchant/problem)

## Tests

```bash
# Install packages
$ pip install -U pip poetry
$ poetry install

# Run tests
$ poetry run pytest --benchmark-skip
```

And no, you shouldn't use `pipenv` anymore. Actually, the plain old `requirements.txt` with `virtualenv` is good enough in most of the situations.

## Bugs

If you find any bug or poor implementation in this repo, please let me know by opening an issue or pull request. Me and my cats would appreciate your help since they provide some random strings which are used in two of test cases.

## Resources

### Books

- [Grokking Algorithms](https://learning.oreilly.com/library/view/grokking-algorithms-an/9781617292231/)
- [A Common-Sense Guide to Data Structures and Algorithms](https://learning.oreilly.com/library/view/a-common-sense-guide/9781680502794/)
- [Data Structures and Algorithms in Python](https://learning.oreilly.com/library/view/data-structures-and/9781118290279/)
- [Cracking the Coding Interview](http://www.crackingthecodinginterview.com/)

### Websites

- [Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)
- [Programiz](https://www.programiz.com/dsa)
- [Tech Interview Handbook](https://yangshun.github.io/tech-interview-handbook/)
- [Visualize Python Code Execution](http://www.pythontutor.com/live.html#mode=edit)
