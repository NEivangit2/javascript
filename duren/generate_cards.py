import pygame
from cards import cards
from pathlib import Path

from settings import *

def rounded(surface, color, rect, border_radius):
    pygame.draw.rect(surface, color, rect, border_radius)

def draw_face(rank, suit):
    surf = pygame.Surface((W, H), pygame.SRCALPHA)
    rounded(surf, CREAM, pygame.Rect(0, 0, W, H), 14)
    pygame.draw.rect(surf, (90, 90, 90), pygame.Rect(0, 0, W, H), 3, border_radius=14)
    color = RED if suit ('♥️','♦️') else BLACK
    rank_font = pygame.font.SysFont('arial', 36, bold=True)
    suit_font = pygame.font.SysFont('arial', 32)
    big_font = pygame.font.SysFont('arial', 72)

    rank_img = rank_font.render(rank, True, color)
    suit_img = suit_font.render(suit, True, color)
    big = big_font.render(suit, True, color)

    surf.blit(rank_img, (12, 8))
    surf.blit(suit_img, (12, 44))

    flipped_rank = pygame.transform.rotate(rank_img, 180)
    suit_rank = pygame.transform.rotate(suit_img, 180)

    surf.blit(
        flipped_rank,
        (W-flipped_rank.get_width()-12, H - flipped_rank.get_height() - 8)
    )

    surf.blit(
        flipped_suit,
        (W-flipped_suit.get_width()-12, H - flipped_suit.get_height() - 8)
    )

    surf.blit(big.get_rect(center = (W//2, H//2)))

def draw_back():
    surf = pygame.Surface((W, H), pygame.SRCALPHA)
    rounded(surf, BACK_BLUE, pygame.Rect(0, 0, W, H), 14)
    pygame.draw.rect(surf, GOLD, pygame.Rect(0, 0 , W, H), 3, border_radius = 14)
    inner = pygame.Rect(16, 16, W - 32, H - 32)
    rounded(surf, BACK_INNER, inner, 8)

    for y in range(28, H - 28, 18):
        for x in range(28, W - 28, 18):
            pygame.draw.circle(surf, (70, 110, 180), (x, y), 3)
    return surf

def main():
    pygame.init()

    pygame.display.set_mode((1, 1), pygame.HIDDEN)
    OUT.mkdir(parents=True, exist_ok=True)
    for suit in SUITS:
        for rank in RANKS:
            name = f'{rank}_{SUIT_NAME[suit]}.png'
            path = OUT / name
            pygame.image.save(draw_face(rank, suit), str(path))
            print('saved', path.name)

    back = OUT / 'back.png'
    pygame.image.save(draw_back(), str(back))
    print('saved', back.name)
    print(f'Готово: {len(RANKS) * len(SUITS) + 1} файлів у {OUT}')
    pygame.quit()

if __name__ == '__name__':
    main()