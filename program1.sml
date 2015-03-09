fun sum_div 3 = 3
  | sum_div n = if n mod 3 = 0 orelse n mod 5 = 0
                then n + sum_div (n-1)
                else sum_div (n - 1 )

fun sum_div_below n = sum_div (n - 1)
