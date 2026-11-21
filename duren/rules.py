# Правила гри

from cards import Card

#значення карт на столі

def table_ranks(pairs):
    ranks = set()
    for attack, defense in pairs:
        ranks.add(attack.rank)
        if defense is not None:
            ranks.add(defense.rank)
    return ranks

#перевірка скільки карт не побито

def unbeaten_count(pairs):
    return sum(1 for _, defense in pairs if defense is None)

#перевірка чи всі карти побито

def all_beaten(pairs):
    return bool(pairs) and unbeaten_count(pairs) == 0

#index першої карти, яка не побита

def first_unbeaten_index(pairs):
    for i, (_, defense) in enumerate(pairs):
        if defense is None:
            return i
    return None

def can_attack(card, pairs, defender_card):
    if len(pairs) >= 6:
        return False
    if unbeaten_count(pairs) + 1 > defender_card:
        return False
    if not pairs:
        return True
    return card.rank in table_ranks(pairs)

#чи карта може захищатися від атаки

def can defend(card, attack_card, trump):
    return card.beats(attack_card, trump)