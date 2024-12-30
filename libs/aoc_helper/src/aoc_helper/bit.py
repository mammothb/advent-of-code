def band_pass(signal: int, low: int, high: int) -> int:
    """Applies a band-pass filter to the bit value of `signal`.

    Args:
        signal: Input signal.
        low: Lower cutoff bit width.
        high: Upper cutoff bit width.

    Return:
        Value of `signal` after applying the band-pass filter.
    """
    if low > high:
        raise ValueError("`low` cannot be larger than `high`")

    mask = ((1 << (high - low + 1)) - 1) << low
    return signal & mask
