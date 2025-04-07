# Discrete Logarithm
Discrete logarithm is defined as $g^k$ = $a$ (mod $p$), where $k$ must be calculated given $a$ is in $Z_p$.

1. $Z_p$ is the set of all integers mod $p$ that are relatively prime to $p$.
2. $g$ is a generator of $p$. It is a value in $Z_p$ where { $value_1^1$, $value_2^2$, ... , $value_n^{p - 1}$ } mod $p$ = $Z_p$. For example, $Z_5$ = {1, 2, 3, 4}, and 2 is a generator of 5 because { $2^1$, $2^2$, $2^3$, $2^4$ } mod 5 = {1, 2, 3, 4} mod 5 = $Z_5$. But 4 is not a generator of 5 because { $4^1$, $4^2$, $4^3$, $4^4$ } mod 5 = {4, 1, 4, 1} mod 5 != $Z_5$.
3. If $p$ = $2q + 1$ where q is a prime number, then $g$ can be more easily found through the condition $value_n^{(p-1)/p_i}$ != 1 (mod $p$). So, if ($value_n^{(p-1)/p_i}$) mod $p$ does not equal to 1 mod $p$ for each value of $p_i$, then $g$ is a generator of $p$. $p_i$ is each factor of $p - 1$, where the factors $p - 1$ and 1 do not need to meet the condition.

The idea is that it is very difficult to find $k$ in $g^k$ = $a$ (mod $p$).
