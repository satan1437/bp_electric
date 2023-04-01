"""
В N корзинах находятся золотые монеты. Корзины пронумерованы числами от 1 до N. Во всех корзинах, кроме одной,
монеты весят по w граммов. В одной корзине монеты фальшивые и весят w–d граммов.
Волшебник берет 1 монету из первой корзины, 2 монеты из второй корзины, и так далее, и,
наконец, N-1 монету из (N-1)-й корзины. Из N-й корзины он не берет ничего.
Он взвешивает взятые монеты и сразу указывает на корзину с фальшивыми монетами.
Напишите программу, которая сможет выполнять такое волшебство.
Дано: четыре целых числа: N, w, d и P – суммарный вес отобранных монет. Найти номер корзины с фальшивыми монетами.
"""
import pytest


def find_fake_basket(N, w, d, P) -> int:  # noqa
	"""
	Time complexity: O(n)
	Space complexity: O(1)
	:param N: Total baskets
	:param w: Coin weight
	:param d: Part of the weight of fake coins
	:param P: Total weight of selected coins
	:return: n False basket index
	"""
	per_sum = 0
	for coins in range(1, N):
		per_sum += coins * w
	return N if per_sum == P else abs(int((P - per_sum) / d))


test_data = [
	(10, 25, 8, 1109, 2),
	(10, 25, 8, 1125, 10),
	(8000, 30, 12, 959879400, 50),
]


@pytest.mark.parametrize('N, w, d, P, expected', test_data)
def test_func(N, w, d, P, expected):  # noqa
	assert find_fake_basket(N, w, d, P) == expected
