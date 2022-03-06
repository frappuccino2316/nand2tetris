load Multi4Mux.hdl,
output-file Multi4Mux.out,
compare-to Multi4Mux.cmp,
output-list a%B1.16.1 b%B1.16.1 c%B1.16.1 d%B1.16.1 sel%B2.2.2 out%B1.16.1;

set a %B0000000000000000, set b %B0000000011111111, set c %B1111111100000000, set d %B1111111111111111, set sel %B00, eval, output;
set a %B0000000000000000, set b %B0000000011111111, set c %B1111111100000000, set d %B1111111111111111, set sel %B01, eval, output;
set a %B0000000000000000, set b %B0000000011111111, set c %B1111111100000000, set d %B1111111111111111, set sel %B10, eval, output;
set a %B0000000000000000, set b %B0000000011111111, set c %B1111111100000000, set d %B1111111111111111, set sel %B11, eval, output;
