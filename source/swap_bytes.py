def swap_bytes(num: int) -> int:
	return ((num & 0xFF) << 8) + (num >> 8)
