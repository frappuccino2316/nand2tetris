load Mux4.hdl,
output-file Mux4.out,
compare-to Mux4.cmp,
output-list a%B1.4.1 b%B1.4.1 sel%B1.1.1 out%B1.4.1;

set a %B0000, set b %B0000, set sel 0, eval, output;
set a %B0011, set b %B0000, set sel 0, eval, output;
set a %B1111, set b %B0000, set sel 0, eval, output;
set a %B1111, set b %B1111, set sel 0, eval, output;
set a %B0000, set b %B1100, set sel 1, eval, output;
set a %B0011, set b %B1111, set sel 1, eval, output;
set a %B1100, set b %B0011, set sel 1, eval, output;
set a %B1111, set b %B1111, set sel 1, eval, output;