#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools


# In[2]:


# CS 212, hw1-1: 7-card stud
#
# -----------------
# User Instructions
#
# Write a function best_hand(hand) that takes a seven
# card hand as input and returns the best possible 5
# card hand. The itertools library has some functions
# that may help you solve this problem.
#
# -----------------
# Grading Notes
# 
# Muliple correct answers will be accepted in cases 
# where the best hand is ambiguous (for example, if 
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).





def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered 
    ranks form a 5-card straight."""
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has 
    exactly n-of-a-kind of. Return None if there 
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None 
    
def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'



# In[3]:


def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    
    "These variables holds a hand and the highest rank for a category of hand"
    SF_hand = []   # variable to hold straight Flush hand
    SF_rank = []   # variable to hold highest rank among straight Flush hands
    
    FK_hand = []
    best_4_rank = []
    k4_hand = []
    
    FH_hand = []
    FH_ranks = []
    
    FL_hand = []
    FL_rank = []
    
    ST_hand = []
    ST_rank = []
    
    K3_hand = []
    K3_rank = []
    
    TP_hand = []
    TP_rank =[]
    
    pair_hand = []
    pair_rank =[]
    HC_card_hand = []
    HC_rank =[]
    
    "Look at all the combinations to see if you have Straight Flush"
    hands = [hand for hand in itertools.combinations(hand, 5)]
    
    for this_hand in hands:
        rank = card_ranks(this_hand)       #Extract for the rank of that hand
        
        "These if fxns verifiy the extraxted rank with the associated hand to each category, When they are in"
        "a category checked if the are the best hand for that category, if they are update the variables"
        if straight(rank) and flush(this_hand):     #Check if Straight and Flush
            "Check for Straight Flush"
            if rank > SF_rank:            # Look if the actual card is greater than the previous
                SF_rank = max(rank, SF_rank)     # If it is, make it the highest rank up to now
                SF_hand = this_hand        # Assign it's card to the straight flush hand
    
        elif kind(4,rank): 
            "Then check for Four of a Kind"
            if rank > best_4_rank:
                k4_hand = [card for card in this_hand if '--23456789TJQKA'[kind(4,rank)] in card]
                k4_hand = k4_hand + [card for card in this_hand if '--23456789TJQKA'[kind(4,rank)] not in card]
                best_4_rank = max(best_4_rank, rank)
                FK_hand = list(k4_hand)
                
        elif kind(3, rank) and kind(2, rank):
            if rank > FH_ranks:
                FH_ranks = max(rank, FH_ranks)
                k2_cards = [card for card in this_hand if '--23456789TJQKA'[kind(2,rank)] in card]
                k3_cards = [card for card in this_hand if '--23456789TJQKA'[kind(3,rank)] in card]
                FH_hand = k2_cards + k3_cards
                
        elif flush(this_hand):
            "Check for the flushs in the cards"
            if flush(this_hand):
                if rank > FL_rank:
                    FL_rank = max(rank, FL_rank)
                    FL_hand = list(this_hand)
                    
        elif straight(rank):
            if rank > ST_rank:
                ST_rank = max(rank, FL_rank)
                ST_hand = list(this_hand)
                
        elif kind(3, rank):
            if rank > K3_rank:
                K3_rank = max(rank, K3_rank)
                K3_hand = list(this_hand)
                
        elif two_pair(rank):
            if rank > TP_rank:
                TP_rank = max(rank, TP_rank)
                TP_hand = [card for card in this_hand if '--23456789TJQKA'[two_pair(rank)[0]] in card]
                TP_hand = TP_hand + [card for card in this_hand if '--23456789TJQKA'[two_pair(rank)[1]] in card]
                TP_hand = TP_hand + [card for card in this_hand if '--23456789TJQKA'[two_pair(rank)[0]] not in card and '--23456789TJQKA'[two_pair(rank)[1]] not in card]
                
        elif kind(2, rank):
            if rank > pair_rank:
                pair_rank = max(rank, pair_rank)
                pair_hand = [card for card in this_hand if '--23456789TJQKA'[kind(2,rank)] in card]
                pair_hand = pair_hand + [card for card in this_hand if '--23456789TJQKA'[kind(2,rank)] not in card]
        else:
            if rank > HC_rank:
                HC_rank = max(rank, pair_rank)
                HC_card_hand = list(this_hand)
    
    "Return values in order of importance if they are assigned"
    if SF_hand:
        return SF_hand
    elif FK_hand:
        return FK_hand
    elif FH_hand:
        return FH_hand
    elif FL_hand:
        return FL_hand
    elif ST_hand:
        return ST_hand
    elif K3_hand:
        return K3_hand
    elif TP_hand:
        return TP_hand
    elif pair_card:
        return pair_card
    else:
        return HC_hand
    
    
# ------------------
# Provided Functions
# 
# You may want to use some of the functions which
# you have already defined in the unit to write 
# your best_hand function.


# In[4]:


def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    return max(itertools.combinations(hand, 5), key=hand_rank)


# In[5]:


print(test_best_hand())


# ## With Jokers

# The card '?B' is the black joker and can only be replaced with a black card
# The card '?R' is the red joker and can only be replaced with a red card

# In[8]:


def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    
    hand = [card if card != '?R' else r+s for r in '23456789TJQKA' for s in 'HD' for card in hand ]
    hand = [card if card != '?B' else r+s for r in '23456789TJQKA' for s in 'SC' for card in hand ]
    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]
    hands = [hand for hand in chunks(hand, 7)]
    all_max = []
    for hand in hands:
        all_max.append(max(itertools.combinations(hand, 5), key=hand_rank))

    return max(all_max, key=hand_rank)


def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_wild_hand passes'

# ------------------
# Provided Functions
# 
# You may want to use some of the functions which
# you have already defined in the unit to write 
# your best_hand function.

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered 
    ranks form a 5-card straight."""
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has 
    exactly n-of-a-kind of. Return None if there 
    is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

def two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None 


# In[48]:


test_best_wild_hand()


# In[103]:


best_wild_hand("6C 7C 8C 9C TC 5C ?B".split())


# In[102]:


best_wild_hand("6C 7C 8C 9C TC 5C ?B".split())

