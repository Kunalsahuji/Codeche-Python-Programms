""""Subscriptions
A new TV streaming service was recently started in Chefland called the Chef-TV.

A group of N friends in Chefland want to buy Chef-TV subscriptions. We know that 6 people can share one Chef-TV subscription. Also, the cost of one Chef-TV subscription is X rupees. Determine the minimum total cost that the group of N friends will incur so that everyone in the group is able to use Chef-TV.

Input Format
~ The first line contains a single integer T — the number of test cases. Then the test cases follow.
~ The first and only line of each test case contains two integers N and X — the size of the group of friends and the cost of one subscription.

Output Format
For each test case, output the minimum total cost that the group will incur so that everyone in the group is able to use Chef-TV.

INPUT           OUTPUT

3
1 100           100
12 250          500
16 135          405

Explanation:
Test case 1: There is only one person in the group. Therefore he will have to buy 1 subscription. Therefore the total cost incurred is 
100.
Test case 2: There are 12 people in the group. Therefore they will have to buy 2 subscriptions. Therefore the total cost incurred is 500.
Test case 3: There are 16 people in the group. Therefore they will have to buy 3 subscriptions. Therefore the total cost incurred is 405.
"""

from math import ceil

for _ in range(int(input("Enter number: "))):
    N, X = map(int, input("Enter Friends and Rupees: ").split())
    sub = ceil(N / 6)
    print(sub * X)
