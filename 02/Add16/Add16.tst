load Add16.hdl,
output-file Add16.out,
compare-to Add16.cmp,
output-list a%B1.16.1 b%B1.16.1 out%B1.16.1;

set a %B0000000000000000, set b %B0000000000000000, eval, output;
set a %B0000000000000000, set b %B0000000011111111, eval, output;
set a %B0000000011111111, set b %B0000000000000000, eval, output;
set a %B0000000011111111, set b %B0000000011111111, eval, output;
set a %B1111111111111111, set b %B0000000000000000, eval, output;
set a %B1111111111111111, set b %B0000000000000001, eval, output;
set a %B0101010101010101, set b %B0101010101010101, eval, output;
set a %B1010101010101010, set b %B1010101010101010, eval, output;
set a %B1111111111111111, set b %B1111111111111111, eval, output;