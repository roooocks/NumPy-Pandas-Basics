def entrance_fee(ages) -> int:
    """
        Calculates the admission fee for the amusement park.
        Parameters:
            ages : List of Ages
        Returns:
            int: The total calculated entry fee.
    """
    kid, adult, senior = 5000, 10000, 7000
    total_fee = 0

    for age in ages:
        if age >= 65:
            total_fee = total_fee + senior
        elif age >= 20:
            total_fee = total_fee + adult
        else:
            total_fee = total_fee + kid
    
    return total_fee