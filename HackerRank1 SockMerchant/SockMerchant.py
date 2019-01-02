"""
File: SockMerchant.py
Assignment: HackerRank1:
Language: python3.7
Author: Renee Veit <rmv4506@rit.edu>
Purpose:
"""

def sockMerchant(n, ar):
    """
    Determine how many pairs of socks with
    matching colors there are
    """
    checked = set()
    pairs = 0
    for idx in range(len(ar)):
        sock = ar[idx]
        for ind in range(idx,len(ar)-1):
            if sock not in checked:
                checked.add(sock)
            if ar[ind+1] == sock:
                pairs += 1
                break
            #break
    return pairs

def main():
    """Main function"""
    n = 9

    ar = [10,20,20,10,10,30,50,10,20]

    print(sockMerchant(n,ar))


main()